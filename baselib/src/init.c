#include "init.h"
#include "utils.h"

int PySchema_ClassInit(PyObject *self, PyObject *args, PyObject *kwds) {

  // get annotations
  PyObject *annotations = PySchema_GetAnnotations(self);
  if (annotations == NULL) {
    return -1;
  }

  // get the number of arguments
  Py_ssize_t num_args = PyTuple_Size(args);
  if (num_args != 1) {
    PyErr_SetString(PyExc_TypeError, "Expected 1 argument");
    return -1;
  }

  // get first argument and check if it is a dict
  PyObject *arg = PyTuple_GetItem(args, 0);
  if (!PyDict_Check(arg)) {
    PyErr_SetString(PyExc_TypeError, "Expected dict");
    return -1;
  }

  // iterate all dict items
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(arg, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);

    // make sure the key is also inside the annotations
    if (!PySchema_ContainAnnotationKey(self, PyUnicode_AsUTF8(key_str))) {
      char error_msg[100];
      sprintf(error_msg, "Attribute \"%s\" not found in annotations",
              PyUnicode_AsUTF8(key_str));
      PyErr_SetString(PyExc_AttributeError, error_msg);
      return -1;
    }

    PyObject *left_type =
        PySchema_GetAnnotationType(self, PyUnicode_AsUTF8(key_str));
    if (left_type == NULL) {
      return -1;
    }
    PyObject *right_type = PyObject_Type(value);
    if (right_type == NULL) {
      return -1;
    }
    // TODO: deal with Sehema = dict case
    if (PyObject_RichCompareBool(left_type, right_type, Py_EQ) == 0) {
      // left and right types are not equal
      // we check if left is a class type and right is an instance of dict
      if (PyType_Check(left_type) && PyDict_Check(value)) {
        // create a new instance of the class and initialize it
        PyObject *instance =
            PyObject_CallObject(left_type, PyTuple_Pack(1, value));
        if (instance == NULL) {
          return -1;
        }
        value = instance;
      } else {
        char error_msg[100];
        sprintf(error_msg, "Expected %s, got %s",
                PyObject_GetNameStr(left_type),
                PyObject_GetNameStr(right_type));
        PyErr_SetString(PyExc_TypeError, error_msg);
        return -1;
      }
    }

    if (PyObject_GenericSetAttr(self, key, value) < 0) {
      return -1;
    }

    Py_DECREF(key_str);
  }

  UNUSED(kwds);
  return 0;
}
