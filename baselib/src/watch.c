#include "watch.h"
#include "init.h"

#include <Python.h>

PyObject *watch(PyObject *self, PyObject *args) {
  UNUSED(self);
  // check if there are 2 arguments
  if (PyTuple_Size(args) != 2) {
    PyErr_SetString(PyExc_TypeError, "Expected 2 arguments");
    return NULL;
  }

  // parse arguments
  // first argument is a list of tuples
  // second argument is a function
  PyObject *list_of_tuples = PyTuple_GetItem(args, 0);
  PyObject *func = PyTuple_GetItem(args, 1);

  // go through the list of tuples, make sure
  // the first element of each tuple is a class
  // and the second element is a string
  for (int i = 0; i < PyList_Size(list_of_tuples); i++) {
    PyObject *tuple = PyList_GetItem(list_of_tuples, i);
    if (!PyTuple_Check(tuple)) {
      PyErr_SetString(PyExc_TypeError, "Expected a tuple");
      return NULL;
    }
    if (PyTuple_Size(tuple) != 2) {
      PyErr_SetString(PyExc_TypeError, "Expected a tuple of size 2");
      return NULL;
    }
    PyObject *class = PyTuple_GetItem(tuple, 0);
    PyObject *attr = PyTuple_GetItem(tuple, 1);
    if (!PyType_Check(class)) {
      PyErr_SetString(PyExc_TypeError, "Expected a class");
      return NULL;
    }
    if (!PyUnicode_Check(attr)) {
      PyErr_SetString(PyExc_TypeError, "Expected a string");
      return NULL;
    }

    // TODO: add watch function
  }

  // clear the error
  PyErr_Clear();
  // return the function
  Py_INCREF(func);
  return func;
}
