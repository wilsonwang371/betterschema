#include "schematypes.h"
#include "init.h"
#include "schema.h"
#include "utils.h"

// a dict object to hold all created schema classes
static PyObject *registered_schemas = NULL;

int PySchema_SchemaTypesInit(PyObject *module) {
  // init dict object to hold all created schema classes
  registered_schemas = PyDict_New();

  if (registered_schemas == NULL) {
    // exit if failed to create dict
    return 1;
  }

  // add variable to module
  PyModule_AddObject(module, "__schemas__",
                     PySchema_GetRegisteredSchemaDictObj());
  return 0;
}

PyObject *PySchema_GetRegisteredSchemaDictObj() { return registered_schemas; }

int PySchema_AddRegisteredSchemaObj(const char *class_name, PyObject *schema) {
  if (PyDict_Contains(registered_schemas, PyUnicode_FromString(class_name)) ==
      1) {
    return 0;
  }
  PyDict_SetItem(registered_schemas, PyUnicode_FromString(class_name), schema);
  return 1;
}

int PySchema_ContainsSchemaObj_WithCStrKey(const char *class_name) {
  // check if class_name is in registered_schemas keys
  if (PyDict_Contains(registered_schemas, PyUnicode_FromString(class_name)) ==
      1) {
    return 1;
  }
  return 0;
}

SchemaType PySchema_ToSchemaType_FromTypeObj(PyObject *typeval) {
  // typeval is a python object that something like
  // int, float, str, bool, list[int], ...
  if (PyType_Check(typeval) != 0) {
    // basic types such as int, float, str, bool
    if ((PyTypeObject *)typeval == &PyLong_Type) {
      return TypeInt;
    } else if ((PyTypeObject *)typeval == &PyFloat_Type) {
      return TypeFloat;
    } else if ((PyTypeObject *)typeval == &PyUnicode_Type) {
      return TypeString;
    } else if ((PyTypeObject *)typeval == &PyBool_Type) {
      return TypeBool;
    } else if ((PyTypeObject *)typeval == &PyDict_Type) {
      return TypeDict;
    } else if ((PyTypeObject *)typeval == &PyList_Type) {
      return TypeList;
    } else if (PySchema_IsValidSchemaTypeObj(typeval)) {
      return TypeSchema;
    }
    // unsupported type
    WARN("Unsupported type name %s\n", PyObject_GetNameStr(typeval));
    return TypeInvalid;
  } else if (strcmp(Py_TYPE(typeval)->tp_name, "types.GenericAlias") == 0) {
    // check for list and dict types
    PyObject *origin = PyObject_GetAttrString(typeval, "__origin__");
    if (PyType_Check(origin) == 0) {
      WARN("Failed to get origin in anno type\n");
      return TypeInvalid;
    }
    // if it is a list or dict type, return typeval
    if ((PyTypeObject *)origin == &PyList_Type) {
      return TypeList;
    }
    if ((PyTypeObject *)origin == &PyDict_Type) {
      return TypeDict;
    }
    // unsupported type
    WARN("Unsupported type\n");
    return TypeInvalid;
  } else if (strcmp(Py_TYPE(typeval)->tp_name, "_UnionGenericAlias") == 0) {
    // check for union types
    PyObject *args = PyObject_GetAttrString(typeval, "__args__");
    if (args == NULL) {
      WARN("Failed to get args\n");
      return TypeInvalid;
    }
    // make sure it is a tuple
    if (!PyTuple_Check(args)) {
      WARN("Expected tuple\n");
      return TypeInvalid;
    }

    // if one of the elements is None, it is optional
    for (Py_ssize_t i = 0; i < PyTuple_Size(args); i++) {
      PyObject *element = PyTuple_GetItem(args, i);
      if (element == NULL) {
        WARN("Failed to get element\n");
        return TypeInvalid;
      }
      if (element == (PyObject *)Py_TYPE(Py_None)) {
        return TypeOptional;
      }
    }

    // union type
    return TypeUnion;
  }
  // unsupported type
  WARN("Unsupported type\n");
  return TypeInvalid;
}

PyObject *PySchema_GetListItemTypeObj(PyObject *typeval) {
  SchemaType type = PySchema_ToSchemaType_FromTypeObj(typeval);
  if (type != TypeList) {
    WARN("Expected list type\n");
    return NULL;
  }
  PyObject *args = PyObject_GetAttrString(typeval, "__args__");
  if (args == NULL) {
    WARN("Failed to get args\n");
    return NULL;
  }
  // make sure it is a tuple
  if (!PyTuple_Check(args)) {
    WARN("Expected tuple\n");
    return NULL;
  }
  // get the first element
  PyObject *first_element = PyTuple_GetItem(args, 0);
  if (first_element == NULL) {
    WARN("Failed to get first element\n");
    return NULL;
  }
  return first_element;
}

SchemaType PySchema_GetListItemType(PyObject *typeval) {
  PyObject *typeobj = PySchema_GetListItemTypeObj(typeval);
  if (typeobj == NULL) {
    return TypeInvalid;
  }
  return PySchema_ToSchemaType_FromTypeObj(typeobj);
}

int PySchema_GetKVTypeObj_FromDictTypeObj(PyObject *typeval, PyObject **key,
                                          PyObject **val) {
  SchemaType type = PySchema_ToSchemaType_FromTypeObj(typeval);
  if (type != TypeDict) {
    WARN("Expected dict type\n");
    return -1;
  }
  PyObject *args = PyObject_GetAttrString(typeval, "__args__");
  if (args == NULL) {
    return -1;
  }
  // make sure it is a tuple
  if (!PyTuple_Check(args)) {
    WARN("Expected tuple\n");
    return -1;
  }
  // get the first element
  PyObject *first_element = PyTuple_GetItem(args, 0);
  if (first_element == NULL) {
    WARN("Failed to get first element\n");
    return -1;
  }
  // get the second element
  PyObject *second_element = PyTuple_GetItem(args, 1);
  if (second_element == NULL) {
    WARN("Failed to get second element\n");
    return -1;
  }
  if (key != NULL) {
    *key = first_element;
  }
  if (val != NULL) {
    *val = second_element;
  }
  return 0;
}

int PySchema_GetKVType_FromDictTypeObj(PyObject *typeval, SchemaType *key,
                                       SchemaType *val) {
  PyObject *keyobj, *valobj;
  if (PySchema_GetKVTypeObj_FromDictTypeObj(typeval, &keyobj, &valobj) != 0) {
    return -1;
  }
  SchemaType keytype = PySchema_ToSchemaType_FromTypeObj(keyobj);
  SchemaType valtype = PySchema_ToSchemaType_FromTypeObj(valobj);
  if (keytype == TypeInvalid || valtype == TypeInvalid) {
    return -1;
  }
  if (key != NULL) {
    *key = keytype;
  }
  if (val != NULL) {
    *val = valtype;
  }
  return 0;
}

size_t PySchema_GetUnionInnerTypeObjSize(PyObject *typeval) {
  SchemaType type = PySchema_ToSchemaType_FromTypeObj(typeval);
  if (type != TypeUnion && type != TypeOptional) {
    WARN("Expected union/optional type\n");
    return 0;
  }
  PyObject *args = PyObject_GetAttrString(typeval, "__args__");
  if (args == NULL) {
    WARN("Failed to get args\n");
    return 0;
  }
  // make sure it is a tuple
  if (!PyTuple_Check(args)) {
    WARN("Expected tuple\n");
    return 0;
  }
  return PyTuple_Size(args);
}

PyObject *PySchema_GetUnionInnerTypeObj_ByIdx(PyObject *typeval, size_t index) {
  SchemaType type = PySchema_ToSchemaType_FromTypeObj(typeval);
  if (type != TypeUnion && type != TypeOptional) {
    WARN("Expected union/optional type\n");
    return NULL;
  }
  PyObject *args = PyObject_GetAttrString(typeval, "__args__");
  if (args == NULL) {
    WARN("Failed to get args\n");
    return NULL;
  }
  // make sure it is a tuple
  if (!PyTuple_Check(args)) {
    WARN("Expected tuple\n");
    return NULL;
  }
  // get the element at index
  PyObject *element = PyTuple_GetItem(args, index);
  if (element == NULL) {
    WARN("Failed to get element\n");
    return NULL;
  }
  return element;
}

SchemaType PySchema_GetUnionInnerType_ByIdx(PyObject *typeval, size_t index) {
  PyObject *typeobj = PySchema_GetUnionInnerTypeObj_ByIdx(typeval, index);
  if (typeobj == NULL) {
    return TypeInvalid;
  }
  return PySchema_ToSchemaType_FromTypeObj(typeobj);
}

int PySchema_IsValidTypeObj(PyObject *typeval) {
  SchemaType type = PySchema_ToSchemaType_FromTypeObj(typeval);
  if (type == TypeInvalid) {
    return 0;
  }
  switch (type) {
  case TypeInt:
  case TypeFloat:
  case TypeString:
  case TypeBool:
  case TypeSchema:
    return 1;
  case TypeList: {
    PyObject *list_type = PySchema_GetListItemTypeObj(typeval);
    if (list_type == NULL) {
      return 0;
    }
    if (PySchema_IsValidTypeObj(list_type)) {
      return 1;
    }
    return 0;
  }
  case TypeDict: {
    PyObject *key_type, *val_type;
    if (PySchema_GetKVTypeObj_FromDictTypeObj(typeval, &key_type, &val_type) !=
        0) {
      return 0;
    }
    if (PySchema_IsValidTypeObj(key_type) &&
        PySchema_IsValidTypeObj(val_type)) {
      return 1;
    }
    return 0;
  }
  case TypeOptional:
  case TypeUnion: {
    size_t size = PySchema_GetUnionInnerTypeObjSize(typeval);
    for (size_t i = 0; i < size; i++) {
      PyObject *union_type = PySchema_GetUnionInnerTypeObj_ByIdx(typeval, i);
      if (union_type == NULL) {
        WARN("Failed to get union inner type by index %ld\n", i);
        return 0;
      }
      if (union_type != (PyObject *)Py_TYPE(Py_None) &&
          !PySchema_IsValidTypeObj(union_type)) {
        return 0;
      }
    }
    return 1;
  }
  default:
    return 0;
  }
}

int PySchema_IsValidSchemaTypeObj(PyObject *obj) {
  if (!PyType_Check(obj)) {
    return 0;
  }
  // go through registered schemas and check if obj is in there
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(registered_schemas, &pos, &key, &value)) {
    if (PyObject_RichCompareBool(obj, value, Py_EQ) == 1) {
      return 1;
    }
  }
  return 0;
}
