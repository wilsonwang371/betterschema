#ifndef _UTILS_H
#define _UTILS_H

#include "base.h"
#include <Python.h>

// Type values
typedef enum {
  TYPE_INT,
  TYPE_FLOAT,
  TYPE_STR,
  TYPE_BOOL,
  TYPE_UNKNOWN
} AnnotationDataType;

int current_global_and_local(PyObject **pGlobal, PyObject **pLocal);

AnnotationDataType str_to_typevalue(const char *str);
const char *typevalue_to_str(AnnotationDataType type);

PyObject *object_name_obj(PyObject *obj);
const char *object_name_cstr(PyObject *obj);

// schema annotation related functions
PyObject *schema_annotations(PyObject *obj);
int schema_contains_annotation(PyObject *obj, const char *attr);
AnnotationDataType schema_annotation_type(PyObject *obj, const char *attr);
int is_valid_annotations(PyObject *annotations);

void print_schema_annotations(PyObject *obj);
void print_schema_attributes(PyObject *obj);
void print_schema_dir(PyObject *obj);
void print_type_dict(PyTypeObject *type);

#endif // _UTILS_H
