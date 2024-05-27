#ifndef _INIT_H
#define _INIT_H

#include "debug.h"
#include "schema.h"
#include <Python.h>

int PySchema_ClassInit(PyObject *self, PyObject *args, PyObject *kwds);

#endif // _INIT_H