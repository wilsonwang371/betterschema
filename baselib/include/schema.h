#ifndef _BASE_H
#define _BASE_H

#include <Python.h>

void PySchema_Init(PyObject *module);

PyObject *schema(PyObject *self, PyObject *args);

#endif // _BASE_H
