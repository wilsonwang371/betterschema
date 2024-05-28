"""Load schemas from external sources."""

import logging
import os
import urllib.request
from pprint import pformat, pprint

import coloredlogs
import yaml


coloredlogs.install()
logger = logging.getLogger(__name__)

# set logging level to debug
logger.setLevel(logging.DEBUG)

K8S_GVK_KEY = "x-kubernetes-group-version-kind"


def gvkdict_get_apiversion(gvk: dict) -> str:
    """Get the API version from a GVK dict."""
    assert "group" in gvk and "version" in gvk and "kind" in gvk
    return f"{gvk['group']}/{gvk['version']}"


def gvkdict_get_kind(gvk: dict) -> str:
    """Get the kind from a GVK dict."""
    assert "kind" in gvk and "version" in gvk and "group" in gvk
    return gvk["kind"]


class SchemaDef:
    """OpenAPI item class."""

    def __init__(self, name: str, schema: dict) -> None:
        """OpenAPI item class."""
        self._name = name
        self._schema = schema

    def raw_schema(self):
        """Return the raw schema."""
        return self._schema

    @property
    def name(self) -> str:
        """Return the name."""
        return self._name

    def imports(self) -> list[str]:
        """Return the import string."""
        return []

    def def_string(self) -> str:
        """Return the definition string."""
        return ""


class K8SSchemaDefProperty:
    """Kubernetes OpenAPI item property class."""

    def __init__(self, name: str, schema: dict, required: bool = False) -> None:
        """Kubernetes OpenAPI item property class."""
        self._name = name
        self._schema = schema
        self._required = required

        self._ref = self._schema.get("$ref", None)
        # remove ref #/definitions/
        if self._ref:
            if not self._ref.startswith("#/definitions/"):
                logger.warning(f"Invalid ref {self._ref}")
            else:
                # remove #/definitions/
                self._ref = self._ref[14:]

        self._type = self._schema.get("type", None)

        self._isref = "$ref" in self._schema

        self._items = self._schema.get("items", None)
        if self._items is not None:
            subtype = self._items.get("$ref", None)
            if subtype is not None and subtype.startswith("#/definitions/"):
                self._items["$ref"] = subtype[14:]

    @property
    def required(self) -> bool:
        """Return the required."""
        return self._required

    @property
    def raw_property(self):
        """Return the raw schema."""
        return self._schema

    @property
    def name(self) -> str:
        """Return the name."""
        return self._name

    @property
    def type_str(self) -> str:
        """Return the type."""
        return self._type

    @property
    def isref(self) -> bool:
        """Return the isref."""
        return self._isref

    @property
    def ref(self) -> str:
        """Return the ref."""
        return self._ref

    @property
    def type(self) -> str:
        """Return the type."""
        res = ""
        if self.type_str == "integer":
            res = "int"
        elif self.type_str == "string":
            res = "str"
        elif self.type_str == "boolean":
            res = "bool"
        elif self.type_str == "array":
            assert self._items is not None
            subtype = self._items.get("type", None)
            if subtype is not None:
                if subtype == "integer":
                    res = "list[int]"
                elif subtype == "string":
                    res = "list[str]"
                elif subtype == "boolean":
                    res = "list[bool]"
                else:
                    raise ValueError(f"Invalid subtype {self._schema}")
            else:
                subtype = self._items.get("$ref", None)
                assert subtype is not None
                logger.warning(f"Array subtype {subtype}")
                res = f"list[{subtype}]".replace(".", "_").replace("-", "_")
        elif self.type_str == "object":
            res = "dict"
        elif self.type_str is None:
            assert self.isref
            res = self.ref.replace(".", "_").replace("-", "_")
        if res == "":
            raise ValueError(f"Invalid type {self._schema}")
        if self.required:
            return res
        return f"core.optional[{res}]"


class K8SSchemaDef(SchemaDef):
    """Kubernetes OpenAPI item class."""

    def __init__(self, name: str, schema: dict) -> None:
        """Kubernetes OpenAPI item class."""
        super().__init__(name, schema)
        self._properties = self._process_properties()
        if "additionalProperties" in self._schema:
            self._additional_properties = self._schema["additionalProperties"]

    def _process_properties(self) -> dict[str, K8SSchemaDefProperty]:
        """Process the properties."""
        if "properties" not in self._schema:
            return {}
        p = self._schema["properties"].copy()
        required_list = []
        if "required" in self._schema:
            required_list = self._schema["required"]
        res = {}
        for k, v in p.items():
            res[k] = K8SSchemaDefProperty(k, v, required=k in required_list)
        return res

    @property
    def gvks(self) -> list:
        """Return the GVKs."""
        assert K8S_GVK_KEY in self._schema
        return self._schema[K8S_GVK_KEY]

    @property
    def properties(self) -> dict[str, K8SSchemaDefProperty]:
        """Return the properties."""
        return self._properties

    @property
    def additional_properties(self) -> dict:
        """Return the additional properties."""
        if not hasattr(self, "_additional_properties"):
            return {}
        return self._additional_properties

    def imports(self) -> list[str]:
        """Return the import string."""
        return [
            "from betterschema import core, render"
        ]

    def def_string(self) -> str:
        """Return the definition string."""
        tmpname = self.name.replace(".", "_").replace("-", "_")
        msg = f"""
@core.schema
class {tmpname}:
    \"\"\"{self.raw_schema()["description"]}\"\"\"
"""
        for k, v in self.properties.items():
            msg += f"    {k}: {v.type}\n"
        return msg


class SchemaDefFactory:
    """OpenAPI item factory class."""

    @staticmethod
    def create(name: str, schema: dict) -> SchemaDef:
        """Create an OpenAPI item."""
        if K8S_GVK_KEY in schema:
            return K8SSchemaDef(name, schema)
        return SchemaDef(name, schema)


class OpenAPISpecLoader:
    """Load schemas from an OpenAPI spec file."""

    def __init__(self, spec_path: str) -> dict:
        """Load schemas from an OpenAPI spec file."""
        if os.path.isfile(spec_path):
            specfile = "file://{}".format(os.path.realpath(spec_path))
        else:
            specfile = spec_path
        req = urllib.request.Request(specfile)
        with urllib.request.urlopen(req) as response:
            spec = yaml.safe_load(response)
        self.data = spec

    @property
    def version(self) -> str:
        """Return the OpenAPI version."""
        if "swagger" in self.data:
            version = self.data["swagger"]
        elif "openapi" in self.data:
            version = self.data["openapi"]
        else:
            raise ValueError("Invalid OpenAPI spec")
        return version

    @property
    def definitions(self) -> dict:
        """Return the definitions."""
        return self.data["definitions"]

    # schema definitions
    def schema_defs(self) -> dict[str, SchemaDef]:
        """Return the definitions as a dict."""
        res = {}
        for k, v in self.definitions.items():
            if "type" not in v:
                logger.warning(f"Type not found for {k} \n{pformat(v)}")
                continue
            res[k] = SchemaDefFactory.create(k, v)
        return res


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json"
    data = OpenAPISpecLoader(url)
    # print(data.version)
    # count = 0
    # available_keys = {}
    # for k,v in data.definitions.items():
    #     print("\n")
    #     print(k)
    #     if "properties" in v and "apiVersion" in v["properties"]:
    #         pprint(v["properties"])
    #     for key in v.keys():
    #         if key not in available_keys:
    #             available_keys[key] = 1
    #         else:
    #             available_keys[key] += 1
    #     count += 1
    #     # if count > 30:
    #     #     break
    # pprint([k for k,v in available_keys.items() if v > 1])

    existing_types = {}
    res = data.schema_defs()

    imports = []
    lines = []
    output = ""
    for i in res.values():
        if isinstance(i, K8SSchemaDef):
            print(i.name)
            # pprint(i.gvks)
            # for j in i.gvks:
            #     print(gvkdict_get_apiversion(j))
            #     print(gvkdict_get_kind(j))
            if len(i.gvks) > 1:
                logger.warning(f"Multiple GVKs found for {i.name}, {i.gvks}")
            for k, v in i.properties.items():
                try:
                    # logger.warning(f"{k}, {v.type}, {v.ref}, {v.raw_property}")
                    existing_types[v.type] = 1
                except Exception as e:
                    logger.error(f"{i.name} {str(e)}")
        tmp = i.imports()
        for j in tmp:
            if j not in imports:
                imports.append(j)
        if i.def_string():
            lines.append(i.def_string())
    output = "\n".join(imports) + "\n\n" + "\n".join(lines)
    print(output)

    # pprint([k for k, v in existing_types.items()])
