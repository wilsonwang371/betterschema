#include "attr.h"
#include "init.h"
#include "utils.h"
#include <Python.h>

#define CLASS_NAME_MAX_LEN 64
#define CLASS_DEF_BUF_SIZE 1024

static PyObject *schema(PyObject *self, PyObject *args) {
  int err = 0;

  PyObject *obj;
  if (!PyArg_ParseTuple(args, "O", &obj)) {
    return NULL; // Failed to parse a Python object argument
  }
  UNUSED(self);

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
  class_type->tp_init = PySchema_ClassDefInit;

  // add annotations to the class type tp_dict
  if (PyDict_SetItemString(class_type->tp_dict, "__annotations__",
                           annotations) < 0) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to set __annotations__");
    err = 1;
    goto out;
  }

  if (!PyCallable_Check(class)) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to create a callable class");
    err = 1;
    goto out;
  }

out:
  free(cls_def_buf);
  if (err)
    return NULL;
  Py_INCREF(class);
  return class;
}

static PyMethodDef Methods[] = {
    {"schema", schema, METH_VARARGS,
     "Create a schema class from defined class"},
    {NULL, NULL, 0, NULL} // Sentinel
};

static struct PyModuleDef module = {PyModuleDef_HEAD_INIT,
                                    "pyskema", // Name of the module
                                    "pyskema module for Python C API",
                                    -1,
                                    Methods,
                                    NULL,
                                    NULL,
                                    NULL,
                                    NULL};

PyMODINIT_FUNC PyInit_pyskema(void) { return PyModule_Create(&module); }
