#include "schema.h"
#include "attr.h"
#include "init.h"
#include "schematypes.h"
#include "string.h"
#include "utils.h"
#include <Python.h>

#define CLASS_NAME_MAX_LEN 64
#define CLASS_DEF_BUF_SIZE 1024

static PyObject *PySchema_lshift(PyObject *, PyObject *);

static PyNumberMethods PySchema_NumberMethods = {
    .nb_lshift = (binaryfunc)PySchema_lshift,
};

void PySchema_Init(PyObject *module) {
  // init dict object to hold all created schema classes
  if (PySchema_SchemaTypesInit(module) < 0) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to init registered schemas");
    return;
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
  PyObject *annotations = PySchema_GetAnnoListObj(obj);
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
  class_name[CLASS_NAME_MAX_LEN - 1] = '\0';
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
    PyErr_SetString(PyExc_RuntimeError,
                    sprintf_static("Failed to get class: %s", class_name));
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
  class_type->tp_as_number = &PySchema_NumberMethods;

  if (PySchema_SetAnnoListObj(class, annotations) == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to set annotations");
    err = 1;
    goto out;
  }

  // if any of the values in annotation is also set in the class, then
  // set the value to the class
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
  PyTypeObject *obj_class = (PyTypeObject *)obj;
  while (PyDict_Next(obj_class->tp_dict, &pos, &key, &value)) {
    if (PySchema_IsValidSchemaTypeObj(value)) {
      if (PyObject_GenericSetAttr(class, key, value) < 0) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to set attribute");
        err = 1;
        goto out;
      }
    }
  }

  if (!PyCallable_Check(class)) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to create a callable class");
    err = 1;
    goto out;
  }

  // add the created class to the schema_classes list, the key is the class name
  PySchema_AddRegisteredSchemaObj(class_name, class);

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

static PyObject *PySchema_lshift(PyObject *self, PyObject *value) {
  // in case of a dict
  if (PyDict_Check(value)) {
    // iterate all dict items and set them as attributes
    PyObject *key, *item;
    Py_ssize_t pos = 0;
    while (PyDict_Next(value, &pos, &key, &item)) {
      // if self object does not have the key attribute
      // then return error
      if (PyObject_GenericGetAttr(self, key) == NULL) {
        PyErr_SetString(PyExc_AttributeError, "Attribute not found");
        return NULL;
      }
      // set the attribute
      if (self->ob_type->tp_setattro(self, key, item) < 0) {
        return NULL;
      }
    }
  } else {
    // return not yet supported error
    PyErr_SetString(PyExc_NotImplementedError, "Not yet supported");
    return NULL;
  }
  // TODO: implement this
  return self;
}
