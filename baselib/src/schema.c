#include "schema.h"
#include "attr.h"
#include "init.h"
#include "string.h"
#include "utils.h"
#include <Python.h>

#define CLASS_NAME_MAX_LEN 64
#define CLASS_DEF_BUF_SIZE 1024

// a dict object to hold all created schema classes
static PyObject *registered_schemas = NULL;

int PySchema_IsPrimitiveType(PyObject *obj) {
  if ((PyTypeObject *)obj == &PyLong_Type ||
      (PyTypeObject *)obj == &PyFloat_Type ||
      (PyTypeObject *)obj == &PyUnicode_Type ||
      (PyTypeObject *)obj == &PyBool_Type) {
    return 1;
  } else {
    return 0;
  }
}

int PySchema_IsSchemaType(PyObject *obj) {
  if (!PyType_Check(obj)) {
    return 0;
  }
  // go through registered schemas and check if obj is in there
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(registered_schemas, &pos, &key, &value)) {
    if (PyObject_RichCompareBool(obj, value, Py_EQ) == 1) {
      return 1;
    }
  }
  return 0;
}

void PySchema_Init() {
  // init dict object to hold all created schema classes
  registered_schemas = PyDict_New();
}

PyObject *PySchema_GetRegisteredSchemas() { return registered_schemas; }

int PySchema_AddRegisteredSchema(const char *class_name, PyObject *schema) {
  if (PyDict_Contains(registered_schemas, PyUnicode_FromString(class_name)) ==
      1) {
    return 0;
  }
  PyDict_SetItem(registered_schemas, PyUnicode_FromString(class_name), schema);
  return 1;
}

int PySchema_ContainsSchemaKey(const char *class_name) {
  // check if class_name is in registered_schemas keys
  if (PyDict_Contains(registered_schemas, PyUnicode_FromString(class_name)) ==
      1) {
    return 1;
  }
  return 0;
}

// Convert a type string to a type value
AnnotationDataType PySchema_ConvertStrToAnnoType(const char *str) {
  if (strcmp(str, "int") == 0) {
    return TYPE_INT;
  } else if (strcmp(str, "float") == 0) {
    return TYPE_FLOAT;
  } else if (strcmp(str, "str") == 0) {
    return TYPE_STR;
  } else if (strcmp(str, "bool") == 0) {
    return TYPE_BOOL;
  } else {
    return TYPE_UNKNOWN;
  }
}

const char *PySchema_ConvertAnnoTypeToStr(AnnotationDataType type) {
  switch (type) {
  case TYPE_INT:
    return "int";
  case TYPE_FLOAT:
    return "float";
  case TYPE_STR:
    return "str";
  case TYPE_BOOL:
    return "bool";
  case TYPE_UNKNOWN:
    return "unknown";
  }
}

PyObject *schema(PyObject *self, PyObject *args) {
  UNUSED(self);
  int err = 0;

  PyObject *obj;
  if (!PyArg_ParseTuple(args, "O", &obj)) {
    return NULL; // Failed to parse a Python object argument
  }

  // find all __annotations__
  PyObject *annotations = PySchema_GetAnnotations(obj);
  if (annotations == NULL) {
    return NULL;
  }

  // return a new python class definition
  char *cls_def_buf = (char *)malloc(CLASS_DEF_BUF_SIZE);
  if (cls_def_buf == NULL) {
    PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory");
    return NULL;
  }

  char class_name[CLASS_NAME_MAX_LEN];
  const char *obj_name = PyObject_GetNameStr(obj);
  if (obj_name == NULL) {
    PyErr_SetString(PyExc_AttributeError, "__name__ not found");
    err = 1;
    goto out;
  }
  strncpy(class_name, obj_name, CLASS_NAME_MAX_LEN);
  if (strlen(class_name) == 0) {
    PyErr_SetString(PyExc_AttributeError, "__name__ not found");
    err = 1;
    goto out;
  }

  sprintf(cls_def_buf, "class %s: pass", class_name);

  PyObject *pGlobal, *pLocal;
  if (!PySys_GetGlobalLocal(&pGlobal, &pLocal)) {
    err = 1;
    goto out;
  }

  PyRun_String(cls_def_buf, Py_file_input, pGlobal, pLocal);
  PyObject *class = PyDict_GetItemString(pLocal, class_name);
  if (class == NULL) {
    char error_msg[100];
    sprintf(error_msg, "Failed to get class: %s", class_name);
    PyErr_SetString(PyExc_RuntimeError, error_msg);
    err = 1;
    goto out;
  }

  // add __setattr__ method to the class
  PyTypeObject *class_type = (PyTypeObject *)class;
  // change setattr and getattr to PySchema_ClassDefSetAttr and
  // PySchema_ClassDefGetAttr
  class_type->tp_setattro = PySchema_ClassDefSetAttr;
  class_type->tp_getattro = PySchema_ClassDefGetAttr;
  class_type->tp_init = PySchema_ClassInit;

  // add annotations to the class type tp_dict
  if (PyDict_SetItemString(class_type->tp_dict, "__annotations__",
                           annotations) < 0) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to set __annotations__");
    err = 1;
    goto out;
  }

  // if any of the values in annotation is also set in the class, then
  // set the value to the class
  // TODO: put them into a special attribute
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *cls_value = PyObject_GenericGetAttr(class, key);
    if (cls_value != NULL) {
      if (PyObject_GenericSetAttr(class, key, cls_value) < 0) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to set attribute");
        err = 1;
        goto out;
      }
    } else {
      // set to none if the value is not set
      if (PyObject_GenericSetAttr(class, key, Py_None) < 0) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to set attribute");
        err = 1;
        goto out;
      }
    }
  }

  // go through all attributes in the class and check if they are schema classes
  // if they are, also create them inside the class
  pos = 0;
  while (PyDict_Next(class_type->tp_dict, &pos, &key, &value)) {
    if (PySchema_IsSchemaType(value)) {
      if (PyObject_GenericSetAttr(class, key, value) < 0) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to set attribute");
        err = 1;
        goto out;
      }
    }
  }

  // add special attribute __pyskema__ to the class
  if (PyDict_SetItemString(class_type->tp_dict, "__pyskema__", Py_True) < 0) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to set __pyskema__");
    err = 1;
    goto out;
  }

  if (!PyCallable_Check(class)) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to create a callable class");
    err = 1;
    goto out;
  }

  // add the created class to the schema_classes list, the key is the class name
  PySchema_AddRegisteredSchema(class_name, class);

out:
  free(cls_def_buf);
  if (err) {
    return NULL;
  }
  // clear error
  PyErr_Clear();
  Py_INCREF(class);
  return class;
}
