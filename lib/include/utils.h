#ifndef _UTILS_H
#define _UTILS_H

#include <Python.h>

// Type values
enum { TYPE_INT, TYPE_FLOAT, TYPE_STR, TYPE_BOOL, TYPE_UNKNOWN };

int current_global_and_local(PyObject **pGlobal, PyObject **pLocal);

int type_str_to_val(const char *str);

int valid_annotations(PyObject *annotations);

#endif // _UTILS_H
