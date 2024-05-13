#include "attr.h"
#include "init.h"
#include "utils.h"
#include "watch.h"

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
    // if dict or list, make sure the element type is correct
    if ((PyTypeObject *)anno_type == &PyList_Type) {
      // make sure the right side element type is correct
      PyObject *anno_element_type =
          PySchema_GetAnnotationElementType(self, name_str_c);
      if (anno_element_type == NULL) {
        return -1;
      }
      // iterate each item in value and check if the type is correct
      Py_ssize_t len = PyList_Size(value);
      for (Py_ssize_t i = 0; i < len; i++) {
        PyObject *item = PyList_GetItem(value, i);
        PyObject *item_type = PyObject_Type(item);
        if (PyObject_RichCompareBool(anno_element_type, item_type, Py_EQ) ==
            0) {
          char error_msg[100];
          sprintf(error_msg, "Expected list element type %s, got %s",
                  PyObject_GetNameStr(anno_element_type),
                  PyObject_GetNameStr(item_type));
          PyErr_SetString(PyExc_TypeError, error_msg);
          return -1;
        }
      }
    } else if ((PyTypeObject *)anno_type == &PyDict_Type) {
      // TODO: check the element type of the dict
      fprintf(stderr, "Dict type not supported yet\n");
      return -1;
    }

    PyObject *old_value = PyObject_GenericGetAttr(self, name);
    if (PyObject_GenericSetAttr(self, name, value) < 0) {
      return -1;
    } else {
      // trigger watch event
      if (PyWatch_OnAttributeUpdate(self, name_str_c, old_value, value) < 0) {
        return -1;
      }
    }
    return 0;
  } else if (PySchema_IsSchemaType(anno_type)) {
    // create a new instance of the class and initialize it
    PyObject *instance = PyObject_CallObject(anno_type, PyTuple_Pack(1, value));
    if (instance == NULL) {
      return -1;
    }
    PyObject *old_value = PyObject_GenericGetAttr(self, name);
    if (PyObject_GenericSetAttr(self, name, instance) < 0) {
      return -1;
    } else {
      // trigger watch event
      if (PyWatch_OnAttributeUpdate(self, name_str_c, old_value, instance) <
          0) {
        return -1;
      }
    }
    return 0;
  }

  char error_msg[100];
  sprintf(error_msg, "Unsupported type while setting attribute %s of type %s",
          name_str_c, ((PyTypeObject *)anno_type)->tp_name);
  PyErr_SetString(PyExc_TypeError, error_msg);
  return -1;
}
