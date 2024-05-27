#ifndef _UTILS_H
#define _UTILS_H

#include "schema.h"
#include <Python.h>

int PySys_GetGlobalLocal(PyObject **pGlobal, PyObject **pLocal);

PyObject *PyObject_GetName(PyObject *obj);
const char *PyObject_GetNameStr(PyObject *obj);

// schema annotation related functions
PyObject *PySchema_GetAnnoListObj(PyObject *obj);
PyObject *PySchema_SetAnnoListObj(PyObject *obj, PyObject *annotations);

int PySchema_IsOptionalAnno_ByCStr(PyObject *obj, const char *attr);

int PySchema_ContainAnnoObj_ByCStr(PyObject *obj, const char *attr);
PyObject *PySchema_GetAnnoObj_ByCStr(PyObject *obj, const char *attr);

// TODO: remove this?
PyObject *PySchema_GetAnnotationType(PyObject *obj, const char *attr);

int PySchema_IsValidAnnotations(PyObject *annotations);

void PySchema_PrintAnnotations(PyObject *obj);
void PySchema_PrintDir(PyObject *obj);
void PySchema_PrintTypeDict(PyTypeObject *type);

const char *sprintf_static(const char *fmt, ...);

#endif // _UTILS_H
