"""Load schemas from external sources."""

import argparse
import logging
import os
import re
import urllib.request
from pprint import pformat

import coloredlogs
import yaml

coloredlogs.install()
logger = logging.getLogger(__name__)

# set logging level to debug
logger.setLevel(logging.DEBUG)

K8S_GVK_KEY = "x-kubernetes-group-version-kind"


def escape_reserved(name: str) -> str:
    """Escape reserved keywords."""
    if name in [
        "from",
        "import",
        "as",
        "global",
        "nonlocal",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "if",
        "lambda",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
        "not",
    ]:
        return f"{name}_"
    return name


def has_special_chars(name: str) -> bool:
    """Check if a name has special characters."""
    return any(c in name for c in "-./\[\]{}()<>+=*&%$#@!")


def escape_special_chars(name: str) -> str:
    """Escape special characters in a name."""
    return (
        name.replace("-", "_")
        .replace(".", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace("[", "_")
        .replace("]", "_")
        .replace("{", "_")
        .replace("}", "_")
        .replace("(", "_")
        .replace(")", "_")
        .replace("<", "_")
        .replace(">", "_")
        .replace("=", "_")
        .replace("+", "_")
        .replace("*", "_")
        .replace("&", "_")
        .replace("%", "_")
        .replace("$", "_")
        .replace("#", "_")
        .replace("@", "_")
        .replace("!", "_")
    )


def pythonize_name(name: str) -> str:
    """Convert a name to a pythonic name."""
    return name.replace("-", "_").replace(".", "_")


def gvkdict_get_apiversion(gvk: dict) -> str:
    """Get the API version from a GVK dict."""
    assert "group" in gvk and "version" in gvk and "kind" in gvk
    return f"{gvk['group']}/{gvk['version']}"


def gvkdict_get_kind(gvk: dict) -> str:
    """Get the kind from a GVK dict."""
    assert "kind" in gvk and "version" in gvk and "group" in gvk
    return gvk["kind"]


class SchemaDefProperty:
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
                logger.warning("Invalid ref %s", self._ref)
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

        self._dependencies = []
        self._type = self._process_type()

    @property
    def dependencies(self) -> list[str]:
        """Return the dependencies."""
        return self._dependencies

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
        return self._type

    def _process_type(self) -> str:
        """Return the type."""
        res = ""
        if self.type_str == "integer":
            res = "int"
        elif self.type_str == "string":
            res = "str"
        elif self.type_str == "boolean":
            res = "bool"
        elif self.type_str == "number":
            res = "float"
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
                res = pythonize_name(f"list[{subtype}]")
                if subtype != self.name:
                    self._dependencies.append(subtype)
        elif self.type_str == "object":
            res = "dict[str, str]"
        elif self.type_str is None:
            assert self.isref
            res = pythonize_name(self.ref)
            if self.ref != self.name:
                self._dependencies.append(self.ref)
        if res == "":
            raise ValueError(f"Invalid type {self._schema}")

        # remove duplicates in dependencies
        self._dependencies = list(set(self._dependencies))
        if self.required:
            return res
        return f"core.Optional[{res}]"


class SchemaDef:
    """OpenAPI item class."""

    def __init__(self, name: str, schema: dict) -> None:
        """OpenAPI item class."""
        self._name = name
        self._schema = schema
        self._mapping = {}
        self._properties = self._process_properties()

    def _process_properties(self) -> dict[str, SchemaDefProperty]:
        """Process the properties."""
        expected_keys = ["type", "properties"]
        no_match = [i for i in expected_keys if i not in self._schema]
        if len(no_match) == len(expected_keys):
            logger.warning(
                "No type nor properties found in "
                + f"{self._name}, exisiting keys: "
                + f"{self._schema.keys()}"
            )
            return {}

        if "properties" in self._schema:
            p = self._schema["properties"].copy()
            required_list = []
            if "required" in self._schema:
                required_list = self._schema["required"]
            res = {}
            for k, v in p.items():
                newk = escape_reserved(k)
                if has_special_chars(newk):
                    newk = escape_special_chars(newk)
                    self._mapping[k] = newk
                res[newk] = SchemaDefProperty(newk, v, required=k in required_list)
            return res
        return {}

    @property
    def description(self) -> str:
        """Return the description."""
        return self._schema["description"] if "description" in self._schema else "N/A"

    @property
    def properties(self) -> dict[str, SchemaDefProperty]:
        """Return the properties."""
        return self._properties

    @property
    def raw_schema(self):
        """Return the raw schema."""
        return self._schema

    @property
    def dependencies(self) -> list[str]:
        """Return the dependencies."""
        res = []
        for v in self.properties.values():
            res.extend(v.dependencies)
        # remove duplicates
        res = list(set(res))
        # remove self
        if self.name in res:
            res.remove(self.name)
        return res

    @property
    def mapping(self) -> dict:
        """Return the mapping."""
        return self._mapping

    @property
    def name(self) -> str:
        """Return the name."""
        return self._name

    def imports(self) -> list[str]:
        """Return the import string."""
        return ["from betterschema import core, render"]

    def def_string(self) -> str:
        """Return the definition string."""
        tmpname = pythonize_name(self.name)
        deps = self.dependencies
        msg = """@core.schema"""
        if self._mapping:
            msg += f"""(
    mapping={pformat(self.mapping, indent=4)},
)"""
        msg += f"""
class {tmpname}:
    \"\"\"{self.description}\"\"\"

    \"\"\"Dependencies: {pformat(deps, indent=4)}\"\"\"
"""
        count = 0
        for k, v in self.properties.items():
            type_str = v.type
            # check if type_str contains tmpname using
            # regex, if so, replace coresponding tmpname substring with 'core.SchemaSelf'
            if re.search(rf"(?<!\w){tmpname}(?!\w)", type_str):
                type_str = re.sub(
                    rf"(?<!\w){tmpname}(?!\w)", "core.SchemaSelf", type_str
                )
            msg += f"    {k}: {type_str}\n"
            count += 1
        if count == 0:
            msg += "    pass\n"
        return msg


class K8SSchemaDef(SchemaDef):
    """Kubernetes OpenAPI item class."""

    def __init__(self, name: str, schema: dict) -> None:
        """Kubernetes OpenAPI item class."""
        super().__init__(name, schema)
        if "additionalProperties" in self._schema:
            self._additional_properties = self._schema["additionalProperties"]

    @property
    def gvks(self) -> list:
        """Return the GVKs."""
        assert K8S_GVK_KEY in self._schema
        return self._schema[K8S_GVK_KEY]

    @property
    def additional_properties(self) -> dict:
        """Return the additional properties."""
        if not hasattr(self, "_additional_properties"):
            return {}
        return self._additional_properties


class SchemaDefFactory:
    """OpenAPI item factory class."""

    @staticmethod
    def create(name: str, schema: dict) -> SchemaDef:
        """Create an OpenAPI item."""
        logger.debug("Creating schema %s", name)
        if K8S_GVK_KEY in schema:
            return K8SSchemaDef(name, schema)
        return SchemaDef(name, schema)


class OpenAPISpecLoader:
    """Load schemas from an OpenAPI spec file."""

    def __init__(self, spec_path: str) -> dict:
        """Load schemas from an OpenAPI spec file."""
        if os.path.isfile(spec_path):
            specfile = f"file://{os.path.realpath(spec_path)}"
        else:
            specfile = spec_path
        req = urllib.request.Request(specfile)
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                spec = yaml.safe_load(response)
        except urllib.error.HTTPError as e:
            logger.error("Error loading %s: %s", specfile, e)
            raise
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
            res[k] = SchemaDefFactory.create(k, v)
        return res


def parse_args():
    """Parse the arguments."""
    parser = argparse.ArgumentParser(description="OpenAPI Schema Converter")
    parser.add_argument(
        "-u",
        "--url",
        help="URL to the OpenAPI spec file",
        default=(
            "https://raw.githubusercontent.com/kubernetes"
            + "/kubernetes/master/api/openapi-spec/swagger.json"
        ),
    )
    # output file
    parser.add_argument(
        "-o",
        "--output",
        help="Output file",
        default="output.py",
    )
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_args()
    data = OpenAPISpecLoader(args.url)

    existing_types = {}
    res = data.schema_defs()

    imports = []
    lines = []
    output = ""

    # sort res based on its dependencies
    # max_iter = 100000
    tmp = {}
    while len(res) > 0:
        keys_to_remove = []
        # for each item in res, check if all its dependencies are in tmp items
        for k, v in res.items():
            deps = v.dependencies
            # print the dependencies not found
            for dep in deps:
                if dep not in res:
                    logger.warning("Dependency %s not found for %s", dep, k)
            # resolve the dependencies
            if all(dep in tmp for dep in deps) or len(deps) == 0:
                tmp[k] = v
                keys_to_remove.append(k)
        if len(keys_to_remove) == 0:
            logger.error(
                "No items can be moved to tmp, remaining " + "keys %s\n items: %s",
                res.keys(),
                [v.dependencies for _, v in res.items()],
            )
            raise ValueError("No items can be moved to tmp")
        for k in keys_to_remove:
            del res[k]
    res = tmp

    for i in res.values():
        if isinstance(i, K8SSchemaDef):
            logger.info("Processing K8s Schema: %s", i.name)
            for k, v in i.properties.items():
                existing_types[v.type] = 1
        else:
            logger.info("Processing Schema: %s", i.name)
            for k, v in i.properties.items():
                existing_types[v.type] = 1
        tmp = i.imports()
        for j in tmp:
            if j not in imports:
                imports.append(j)
        if i.def_string():
            lines.append(i.def_string())
    output = "\n".join(imports) + "\n\n" + "\n".join(lines)

    # output to file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    main()
