#ifndef _ATTR_H

#define _ATTR_H
#include <Python.h>

#include "base.h"

int schema_setattr(PyObject *, PyObject *, PyObject *);
PyObject *schema_getattr(PyObject *self, PyObject *name);

#endif // _ATTR_H