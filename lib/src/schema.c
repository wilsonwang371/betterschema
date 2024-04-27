#include <Python.h>

#define UNUSED(x) (void)(x)

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

enum { TYPE_INT, TYPE_FLOAT, TYPE_STR, TYPE_BOOL, TYPE_UNKNOWN };

static int str_to_type(const char *str) {
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

int valid_annotations(PyObject *annotations) {
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  char error_msg[100];
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str = PyObject_GetAttrString(value, "__name__");

    switch (str_to_type(PyUnicode_AsUTF8(value_str))) {
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
    printf("key: %s, value: %s\n", key_str_c, value_str_c);
    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
  return 1;
}

static PyObject *schema(PyObject *self, PyObject *args) {
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
  }

  if (!valid_annotations(annotations)) {
    return NULL;
  }

  // return a new python class definition
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  char new_class_def[5000];
  char annotations_str[5000];
  sprintf(new_class_def, "class %s: \n",
          PyUnicode_AsUTF8(PyObject_GetAttrString(obj, "__name__")));
  // for each of the annotations, add using @property and setter to the class
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str = PyObject_GetAttrString(value, "__name__");
    char key_str_c[100];
    char value_str_c[100];
    sprintf(key_str_c, "%s", PyUnicode_AsUTF8(key_str));
    sprintf(value_str_c, "%s", PyUnicode_AsUTF8(value_str));

    sprintf(annotations_str + strlen(annotations_str), "%s: %s, ", key_str_c,
            value_str_c);

    sprintf(new_class_def + strlen(new_class_def), TYPE_CHECKED_PROPERTY_TMPL,
            key_str_c, key_str_c, key_str_c, key_str_c, value_str_c,
            value_str_c, key_str_c);

    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }

  // add __annotations__ to the class
  sprintf(new_class_def + strlen(new_class_def), "    __annotations__ = {%s}\n",
          annotations_str);

  printf("%s\n", new_class_def);

  // Get the current frame
  PyFrameObject *currentFrame = PyEval_GetFrame();
  if (currentFrame == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to get the current frame");
    return NULL;
  }

  // Access the global and local dictionaries
  PyObject *pGlobal = PyFrame_GetGlobals(currentFrame);
  PyObject *pLocal = PyFrame_GetLocals(currentFrame);
  PyRun_String(new_class_def, Py_file_input, pGlobal, pLocal);

  PyObject *class = PyDict_GetItemString(
      pLocal, PyUnicode_AsUTF8(PyObject_GetAttrString(obj, "__name__")));
  if (class == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to create a class");
    return NULL;
  }

  if (PyCallable_Check(class)) {
    return class;
  } else {
    PyErr_SetString(PyExc_RuntimeError, "Failed to create a callable class");
    return NULL;
  }
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
