#ifndef _BASE_H
#define _BASE_H

#include <Python.h>

int PySchema_IsPrimitiveType(PyObject *obj);
int PySchema_IsSchemaType(PyObject *obj);

void PySchema_Init(PyObject *module);
PyObject *PySchema_GetRegisteredSchemas();
int PySchema_AddRegisteredSchema(const char *class_name, PyObject *schema);
int PySchema_ContainsSchemaKey(const char *class_name);

// Type values
typedef enum {
  TYPE_INT,
  TYPE_FLOAT,
  TYPE_STR,
  TYPE_BOOL,
  TYPE_UNKNOWN
} AnnotationDataType;

AnnotationDataType PySchema_ConvertStrToAnnoType(const char *str);
const char *PySchema_ConvertAnnoTypeToStr(AnnotationDataType type);

PyObject *schema(PyObject *self, PyObject *args);

#endif // _BASE_H
