#ifndef _WATCH_H

#define _WATCH_H

#include <Python.h>

void PyWatch_Init(PyObject *module);

PyObject *PyWatch_GetWatchDict();

PyObject *watch(PyObject *self, PyObject *args);

#endif // _WATCH_H
