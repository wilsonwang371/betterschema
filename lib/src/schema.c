#include "utils.h"
#include <Python.h>

#define UNUSED(x) (void)(x)

#define CLASS_NAME_MAX_LEN 64
#define CLASS_DEF_BUF_SIZE 4096 * 4

#define INIT_FUNC_TMPL                                                         \
  "    def __init__(self, %s: dict): \n"                                       \
  "        if not isinstance(%s, dict): \n"                                    \
  "            raise ValueError('Expected dict')\n"

#define TYPE_CHECKED_PROPERTY_TMPL                                             \
  "    @property\n    def %s(self): \n"                                        \
  "        return self.__dict__['%s']\n\n"                                     \
  "    @%s.setter\n    def %s(self, value): \n"                                \
  "        if not isinstance(value, %s): \n"                                   \
  "            raise ValueError('Expected %s')\n"                              \
  "        self.__dict__['%s'] = value\n\n"

static int annotation_to_class_properties(PyObject *annotations, char *buf,
                                          size_t buf_len) {
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  char error_msg[100];
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str = PyObject_GetAttrString(value, "__name__");

    switch (type_str_to_val(PyUnicode_AsUTF8(value_str))) {
    case TYPE_INT:
    case TYPE_FLOAT:
    case TYPE_STR:
    case TYPE_BOOL:
      break;
    case TYPE_UNKNOWN:
      sprintf(error_msg, "Unsupported type: %s", PyUnicode_AsUTF8(value_str));
      PyErr_SetString(PyExc_TypeError, error_msg);
      return 0;
    }

    char key_str_c[100];
    char value_str_c[100];
    sprintf(key_str_c, "%s", PyUnicode_AsUTF8(key_str));
    sprintf(value_str_c, "%s", PyUnicode_AsUTF8(value_str));

    snprintf(buf + strlen(buf), buf_len - strlen(buf),
             TYPE_CHECKED_PROPERTY_TMPL, key_str_c, key_str_c, key_str_c,
             key_str_c, value_str_c, value_str_c, key_str_c);
    if (strlen(buf) >= buf_len) {
      PyErr_SetString(PyExc_RuntimeError, "Buffer overflow");
      return 0;
    }

    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
  return 1;
}

static PyObject *schema(PyObject *self, PyObject *args) {
  int err = 0;

  PyObject *obj;
  if (!PyArg_ParseTuple(args, "O", &obj)) {
    return NULL; // Failed to parse a Python object argument
  }
  UNUSED(self);

  // find all __annotations__
  PyObject *annotations = PyObject_GetAttrString(obj, "__annotations__");
  if (annotations == NULL) {
    PyErr_SetString(PyExc_AttributeError, "__annotations__ not found");
    return NULL;
  } else {
    if (!valid_annotations(annotations)) {
      return NULL;
    }
  }

  // return a new python class definition
  char *cls_def_buf = (char *)malloc(CLASS_DEF_BUF_SIZE);
  if (cls_def_buf == NULL) {
    PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory");
    return NULL;
  }

  char class_name[CLASS_NAME_MAX_LEN];
  strncpy(class_name, PyUnicode_AsUTF8(PyObject_GetAttrString(obj, "__name__")),
          CLASS_NAME_MAX_LEN);
  if (strlen(class_name) == 0) {
    PyErr_SetString(PyExc_AttributeError, "__name__ not found");
    err = 1;
    goto out;
  }

  sprintf(cls_def_buf, "class %s: \n", class_name);
  if (!annotation_to_class_properties(
          annotations, cls_def_buf + strlen(cls_def_buf),
          sizeof(cls_def_buf) - strlen(cls_def_buf))) {
    err = 1;
    goto out;
  }

  printf("%s\n", cls_def_buf);

  PyObject *pGlobal, *pLocal;
  if (!current_global_and_local(&pGlobal, &pLocal)) {
    err = 1;
    goto out;
  }

  PyRun_String(cls_def_buf, Py_file_input, pGlobal, pLocal);
  PyObject *class = PyDict_GetItemString(pLocal, class_name);
  if (class == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to create a class");
    err = 1;
    goto out;
  }

  // add annotations object to the class
  PyObject_SetAttrString(class, "__annotations__", annotations);
  Py_DECREF(annotations);

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
                                    "pylatform", // Name of the module
                                    "Pylatform module for Python C API",
                                    -1,
                                    Methods,
                                    NULL,
                                    NULL,
                                    NULL,
                                    NULL};

PyMODINIT_FUNC PyInit_pylatform(void) { return PyModule_Create(&module); }
