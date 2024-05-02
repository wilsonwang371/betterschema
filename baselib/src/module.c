#include "attr.h"
#include "init.h"
#include "schema.h"
#include "utils.h"
#include "watch.h"
#include <Python.h>

static PyMethodDef Methods[] = {
    {"schema", schema, METH_VARARGS,
     "Create a schema class from defined class"},
    {"watch", watch, METH_VARARGS, "Watch variable changes"},
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

PyMODINIT_FUNC PyInit_baselib(void) {
  // init dict object to hold all created schema classes
  PySchema_Init();

  return PyModule_Create(&module);
}
