#ifndef __SCHEMATYPES_H
#define __SCHEMATYPES_H

#include <Python.h>

#define MAX_UNION_TYPES 10

typedef enum {
  TypeInt = 1,
  TypeFloat,
  TypeString,
  TypeBool,
  TypeSchema,
  TypeList,
  TypeDict,
  TypeOptional,
  TypeUnion,
  TypeInvalid,
} SchemaType;

int PySchema_SchemaTypesInit(PyObject *module);

PyObject *PySchema_GetRegisteredSchemaDictObj();
int PySchema_AddRegisteredSchemaObj(const char *class_name, PyObject *schema);
int PySchema_ContainsSchemaObj_WithCStrKey(const char *class_name);

SchemaType PySchema_ToSchemaType_FromTypeObj(PyObject *typeval);

// list type related functions
PyObject *PySchema_GetListItemTypeObj(PyObject *typeval);
SchemaType PySchema_GetListItemType(PyObject *typeval);

// dict type related functions
int PySchema_GetKVTypeObj_FromDictTypeObj(PyObject *typeval, PyObject **key,
                                          PyObject **val);
int PySchema_GetKVType_FromDictTypeObj(PyObject *typeval, SchemaType *key,
                                       SchemaType *val);

// union type related functions
size_t PySchema_GetUnionInnerTypeObjSize(PyObject *typeval);
PyObject *PySchema_GetUnionInnerTypeObj_ByIdx(PyObject *typeval, size_t index);
SchemaType PySchema_GetUnionInnerType_ByIdx(PyObject *typeval, size_t index);

int PySchema_IsValidTypeObj(PyObject *typeval);
int PySchema_IsValidSchemaTypeObj(PyObject *obj);

#endif // __SCHEMATYPES_H
