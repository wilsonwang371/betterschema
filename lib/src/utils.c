#include "utils.h"

// Get the current thread frame global and local
int current_global_and_local(PyObject **pGlobal, PyObject **pLocal) {
  // Get the current frame
  PyFrameObject *currentFrame = PyEval_GetFrame();
  if (currentFrame == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to get the current frame");
    return 0;
  }

  // Access the global and local dictionaries
  *pGlobal = PyFrame_GetGlobals(currentFrame);
  *pLocal = PyFrame_GetLocals(currentFrame);
  if (*pGlobal == NULL || *pLocal == NULL) {
    PyErr_SetString(PyExc_RuntimeError,
                    "Failed to get the global and local dictionaries");
    return 0;
  }
  return 1;
}

// Convert a type string to a type value
int type_str_to_val(const char *str) {
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
    printf("key: %s, value: %s\n", key_str_c, value_str_c);
    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
  return 1;
}
