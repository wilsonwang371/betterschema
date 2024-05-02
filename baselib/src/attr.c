#include "attr.h"
#include "init.h"
#include "utils.h"

// getattr
PyObject *PySchema_ClassDefGetAttr(PyObject *self, PyObject *name) {
  // get self annotations
  if (PySchema_GetAnnotations(self) == NULL) {
    return NULL;
  }

  // get the name of the attribute
  PyObject *name_str = PyObject_Str(name);
  char name_str_c[100];
  sprintf(name_str_c, "%s", PyUnicode_AsUTF8(name_str));
  Py_DECREF(name_str);

  // check if the attribute is in the annotations
  int has_attr = PySchema_ContainAnnotationKey(self, name_str_c);
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

  PyObject *anno_type = PySchema_GetAnnotationType(self, name_str_c);
  if (anno_type == NULL) {
    return NULL;
  }
  if (PySchema_IsPrimitiveType(anno_type) || PySchema_IsSchemaType(anno_type)) {
    return PyObject_GenericGetAttr(self, name);
  }

  char error_msg[100];
  sprintf(error_msg, "Unsupported type while getting attribute %s of type %s",
          name_str_c, ((PyTypeObject *)anno_type)->tp_name);
  PyErr_SetString(PyExc_TypeError, error_msg);
  return NULL;
}

int PySchema_ClassDefSetAttr(PyObject *self, PyObject *name, PyObject *value) {
  // get self annotations
  if (PySchema_GetAnnotations(self) == NULL) {
    return -1;
  }

  // get the name of the attribute
  PyObject *name_str = PyObject_Str(name);
  char name_str_c[100];
  sprintf(name_str_c, "%s", PyUnicode_AsUTF8(name_str));
  Py_DECREF(name_str);

  // check if the attribute is in the annotations
  int has_attr = PySchema_ContainAnnotationKey(self, name_str_c);
  if (!has_attr) {
    char error_msg[100];
    sprintf(error_msg, "Attribute \"%s\" not found while setting attr",
            name_str_c);
    PyErr_SetString(PyExc_AttributeError, error_msg);
    return -1;
  }

  PyObject *right_type = PyObject_Type(value);
  if (right_type == NULL) {
    return -1;
  }
  PyObject *anno_type = PySchema_GetAnnotationType(self, name_str_c);
  if (anno_type == NULL) {
    return -1;
  }
  if (PySchema_IsPrimitiveType(anno_type)) {
    if (PyObject_RichCompareBool(anno_type, right_type, Py_EQ) == 0) {
      char error_msg[100];
      sprintf(error_msg, "Expected %s, got %s", PyObject_GetNameStr(anno_type),
              PyObject_GetNameStr(right_type));
      PyErr_SetString(PyExc_TypeError, error_msg);
      return -1;
    }
    return PyObject_GenericSetAttr(self, name, value);
  }
  if (PySchema_IsSchemaType(anno_type)) {
    // create a new instance of the class and initialize it
    PyObject *instance = PyObject_CallObject(anno_type, PyTuple_Pack(1, value));
    if (instance == NULL) {
      return -1;
    }
    return PyObject_GenericSetAttr(self, name, instance);
  }

  char error_msg[100];
  sprintf(error_msg, "Unsupported type while setting attribute %s of type %s",
          name_str_c, ((PyTypeObject *)anno_type)->tp_name);
  PyErr_SetString(PyExc_TypeError, error_msg);
  return -1;
}
