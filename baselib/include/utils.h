#ifndef _UTILS_H
#define _UTILS_H

#include "schema.h"
#include <Python.h>

int PySys_GetGlobalLocal(PyObject **pGlobal, PyObject **pLocal);

PyObject *PyObject_GetName(PyObject *obj);
const char *PyObject_GetNameStr(PyObject *obj);

// schema annotation related functions
PyObject *PySchema_GetAnnotations(PyObject *obj);
int PySchema_ContainAnnotationKey(PyObject *obj, const char *attr);
PyObject *PySchema_GetAnnotationType(PyObject *obj, const char *attr);
AnnotationDataType PySchema_GetAnnotationValType(PyObject *obj,
                                                 const char *attr);
int PySchema_IsValidAnnotations(PyObject *annotations);

void PySchema_PrintAnnotations(PyObject *obj);
void PySchema_PrintDir(PyObject *obj);
void PySchema_PrintTypeDict(PyTypeObject *type);

#endif // _UTILS_H
