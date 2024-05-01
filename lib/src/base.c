#include "base.h"
#include "string.h"
#include <Python.h>

// a dict object to hold all created schema classes
static PyObject *registered_schemas = NULL;

int PySchema_IsPrimitiveType(PyObject *obj) {
  if ((PyTypeObject *)obj == &PyLong_Type ||
      (PyTypeObject *)obj == &PyFloat_Type ||
      (PyTypeObject *)obj == &PyUnicode_Type ||
      (PyTypeObject *)obj == &PyBool_Type) {
    return 1;
  } else {
    return 0;
  }
}

int PySchema_IsSchemaType(PyObject *obj) {
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

void PySchema_Init() {
  // init dict object to hold all created schema classes
  registered_schemas = PyDict_New();
}

PyObject *PySchema_GetRegisteredSchemas() { return registered_schemas; }

int PySchema_AddRegisteredSchema(const char *class_name, PyObject *schema) {
  if (PyDict_Contains(registered_schemas, PyUnicode_FromString(class_name)) ==
      1) {
    return 0;
  }
  PyDict_SetItem(registered_schemas, PyUnicode_FromString(class_name), schema);
  return 1;
}

int PySchema_ContainsSchemaKey(const char *class_name) {
  // check if class_name is in registered_schemas keys
  if (PyDict_Contains(registered_schemas, PyUnicode_FromString(class_name)) ==
      1) {
    return 1;
  }
  return 0;
}

// Convert a type string to a type value
AnnotationDataType PySchema_ConvertStrToAnnoType(const char *str) {
  if (strcmp(str, "int") == 0) {
    return TYPE_INT;
  } else if (strcmp(str, "float") == 0) {
    return TYPE_FLOAT;
  } else if (strcmp(str, "str") == 0) {
    return TYPE_STR;
  } else if (strcmp(str, "bool") == 0) {
    return TYPE_BOOL;
  } else {
    return TYPE_UNKNOWN;
  }
}

const char *PySchema_ConvertAnnoTypeToStr(AnnotationDataType type) {
  switch (type) {
  case TYPE_INT:
    return "int";
  case TYPE_FLOAT:
    return "float";
  case TYPE_STR:
    return "str";
  case TYPE_BOOL:
    return "bool";
  case TYPE_UNKNOWN:
    return "unknown";
  }
}
