#include "attr.h"
#include "utils.h"

// getattr
PyObject *schema_getattr(PyObject *self, PyObject *name) {
  // get self annotations
  if (schema_annotations(self) == NULL) {
    return NULL;
  }

  // get the name of the attribute
  PyObject *name_str = PyObject_Str(name);
  char name_str_c[100];
  sprintf(name_str_c, "%s", PyUnicode_AsUTF8(name_str));
  Py_DECREF(name_str);

  // check if the attribute is in the annotations
  int has_attr = schema_contains_annotation(self, name_str_c);
  if (!has_attr) {
    // check if the attribute has __ prefix
    if (name_str_c[0] == '_' && name_str_c[1] == '_') {
      return PyObject_GenericGetAttr(self, name);
    }
    char error_msg[100];
    sprintf(error_msg, "Attribute %s not found while getting attr", name_str_c);
    PyErr_SetString(PyExc_AttributeError, error_msg);
    return NULL;
  }

  // get the type of the attribute
  AnnotationDataType attr_type = schema_annotation_type(self, name_str_c);
  switch (attr_type) {
  case TYPE_INT:
  case TYPE_FLOAT:
  case TYPE_STR:
  case TYPE_BOOL:
    return PyObject_GenericGetAttr(self, name);
  default:
    PyErr_SetString(PyExc_TypeError, "Unsupported type");
    return NULL;
  }
}

int schema_setattr(PyObject *self, PyObject *name, PyObject *value) {
  int res = 0;
  // get self annotations
  if (schema_annotations(self) == NULL) {
    return -1;
  }

  // get the name of the attribute
  PyObject *name_str = PyObject_Str(name);
  char name_str_c[100];
  sprintf(name_str_c, "%s", PyUnicode_AsUTF8(name_str));
  Py_DECREF(name_str);

  // check if the attribute is in the annotations
  int has_attr = schema_contains_annotation(self, name_str_c);
  if (!has_attr) {
    char error_msg[100];
    sprintf(error_msg, "Attribute \"%s\" not found while setting attr",
            name_str_c);
    PyErr_SetString(PyExc_AttributeError, error_msg);
    return -1;
  }
  // fprintf(stderr, "Attribute \"%s\" found\n", name_str_c);

  // get the type of the attribute
  AnnotationDataType attr_type = schema_annotation_type(self, name_str_c);
  switch (attr_type) {
  case TYPE_INT:
    if (!PyLong_Check(value)) {
      PyErr_SetString(PyExc_TypeError, "Attribute must be an integer");
      return -1;
    }
    res = PyObject_GenericSetAttr(self, name, value);
    break;
  case TYPE_FLOAT:
    if (!PyFloat_Check(value)) {
      PyErr_SetString(PyExc_TypeError, "Attribute must be a float");
      return -1;
    }
    res = PyObject_GenericSetAttr(self, name, value);
    break;
  case TYPE_STR:
    if (!PyUnicode_Check(value)) {
      PyErr_SetString(PyExc_TypeError, "Attribute must be a string");
      return -1;
    }
    res = PyObject_GenericSetAttr(self, name, value);
    break;
  case TYPE_BOOL:
    if (!PyBool_Check(value)) {
      PyErr_SetString(PyExc_TypeError, "Attribute must be a boolean");
      return -1;
    }
    res = PyObject_GenericSetAttr(self, name, value);
    break;
  default:
    PyErr_SetString(PyExc_TypeError, "Unsupported type");
    return -1;
  }
  return res;
}
