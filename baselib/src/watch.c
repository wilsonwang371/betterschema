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

  // check the number of arguments supported by the function is the same as the
  // number of tuples
  if (PyFunction_Check(func) == 0) {
    PyErr_SetString(PyExc_TypeError, "Expected a function");
    return NULL;
  }
  PyObject *code = PyFunction_GetCode(func);
  if (code == NULL) {
    PyErr_SetString(PyExc_TypeError, "Expected a function");
    return NULL;
  }
  PyObject *argcount = PyObject_GetAttrString(code, "co_argcount");
  if (argcount == NULL) {
    PyErr_SetString(PyExc_TypeError, "Expected a function");
    return NULL;
  }
  if (PyLong_Check(argcount) == 0) {
    PyErr_SetString(PyExc_TypeError,
                    "Expected a function with an integer argcount");
    return NULL;
  }
  if (PyLong_AsLong(argcount) != PyList_Size(list_of_tuples)) {
    char buf[100];
    snprintf(buf, 100, "Expected a function with %ld arguments but got %ld",
             PyList_Size(list_of_tuples), PyLong_AsLong(argcount));
    PyErr_SetString(PyExc_TypeError, buf);
    return NULL;
  }

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
