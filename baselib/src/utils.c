#include "utils.h"
#include "schema.h"

// Get the current thread frame global and local
int PySys_GetGlobalLocal(PyObject **pGlobal, PyObject **pLocal) {
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

PyObject *PyObject_GetName(PyObject *obj) {
  return PyObject_GenericGetAttr(obj, PyUnicode_FromString("__name__"));
}

const char *PyObject_GetNameStr(PyObject *obj) {
  PyObject *name = PyObject_GetName(obj);
  if (name == NULL) {
    PyErr_SetString(PyExc_AttributeError, "__name__ not found");
    return NULL;
  }
  return PyUnicode_AsUTF8(name);
}

PyObject *PySchema_GetAnnotations(PyObject *obj) {
  PyTypeObject *type;
  if (PyType_Check(obj) == 0) {
    type = Py_TYPE(obj);
  } else {
    // type object
    type = (PyTypeObject *)obj;
  }
  if (type == NULL) {
    fprintf(stderr, "Failed to get type in get annotations\n");
    return NULL;
  }

  PyObject *annotations =
      PyDict_GetItemString(type->tp_dict, "__annotations__");
  if (annotations == NULL) {
    PyErr_SetString(PyExc_AttributeError, "__annotations__ not found");
    return NULL;
  } else {
    if (!PySchema_IsValidAnnotations(annotations)) {
      fprintf(stderr, "Invalid annotations\n");
      return NULL;
    }
  }

  return annotations;
}

int PySchema_ContainAnnotationKey(PyObject *obj, const char *attr) {
  PyObject *annotations = PySchema_GetAnnotations(obj);
  if (annotations == NULL) {
    fprintf(stderr, "Failed to get annotations while checking annotation\n");
    return 0;
  }
  PyObject *attr_str = PyUnicode_FromString(attr);
  int has_attr = PyDict_Contains(annotations, attr_str);
  Py_DECREF(attr_str);
  return has_attr;
}

PyObject *PySchema_GetAnnotationType(PyObject *obj, const char *attr) {
  PyObject *annotations = PySchema_GetAnnotations(obj);
  if (annotations == NULL) {
    fprintf(stderr,
            "Failed to get annotations while getting annotation type\n");
    return NULL;
  }

  PyObject *typeval = PyDict_GetItemString(annotations, attr);
  if (typeval == NULL) {
    fprintf(stderr, "Failed to get type while getting item %s\n", attr);
    return NULL;
  }
  if (PyType_Check(typeval) == 0) {
    // check if it is a type.GerericAlias
    if (PyObject_HasAttrString(typeval, "__origin__")) {
      PyObject *origin = PyObject_GetAttrString(typeval, "__origin__");
      if (PyType_Check(origin) == 0) {
        fprintf(stderr, "Failed to get origin\n");
        return NULL;
      }
      // if it is a list or dict type, return typeval
      if ((PyTypeObject *)origin == &PyList_Type ||
          (PyTypeObject *)origin == &PyDict_Type) {
        return origin;
      }
    } else {
      fprintf(stderr, "Failed type checking\n");
      return NULL;
    }
  }

  return typeval;
}

PyObject *PySchema_GetAnnotationElementType(PyObject *obj, const char *attr) {
  PyObject *annotations = PySchema_GetAnnotations(obj);
  if (annotations == NULL) {
    fprintf(stderr,
            "Failed to get annotations while getting annotation type\n");
    return NULL;
  }

  PyObject *typeval = PyDict_GetItemString(annotations, attr);
  if (typeval == NULL) {
    fprintf(stderr, "Failed to get type while getting item %s\n", attr);
    return NULL;
  }
  if (PyType_Check(typeval) == 0) {
    // check if it is a type.GerericAlias
    if (PyObject_HasAttrString(typeval, "__origin__")) {
      PyObject *origin = PyObject_GetAttrString(typeval, "__origin__");
      if (PyType_Check(origin) == 0) {
        fprintf(stderr, "Failed to get origin\n");
        return NULL;
      }
      // if it is a list or dict type, return typeval
      if ((PyTypeObject *)origin == &PyList_Type) {
        // get __args__[0] from typeval
        PyObject *args = PyObject_GetAttrString(typeval, "__args__");
        if (args == NULL) {
          fprintf(stderr, "Failed to get args\n");
          return NULL;
        }
        PyObject *element_type = PyTuple_GetItem(args, 0);
        if (element_type == NULL) {
          fprintf(stderr, "Failed to get element type\n");
          return NULL;
        }
        return element_type;
      } else if ((PyTypeObject *)origin == &PyDict_Type) {
        // TODO: get the element type of the dict
        fprintf(stderr, "Dict type not supported yet\n");
        return NULL;
      }
    }
  }

  return NULL;
}

int PySchema_IsValidAnnotations(PyObject *annotations) {
  PyObject *key, *value;
  PyObject *schema = PySchema_GetRegisteredSchemas();
  Py_ssize_t pos = 0;
  char error_msg[100];

  if (schema == NULL) {
    return 0;
  }

  while (PyDict_Next(annotations, &pos, &key, &value)) {
    // check if value has origin
    if (PyObject_HasAttrString(value, "__origin__")) {
      PyObject *origin = PyObject_GetAttrString(value, "__origin__");
      if (PyType_Check(origin) == 0) {
        sprintf(error_msg, "Failed to get origin");
        PyErr_SetString(PyExc_AttributeError, error_msg);
        return 0;
      }
      value = origin;
    }

    // check if primitive type
    if (!PySchema_IsPrimitiveType(value)) {
      // check if schema type
      if (!PySchema_IsSchemaType(value)) {
        sprintf(error_msg, "Unsupported type: %s",
                PyUnicode_AsUTF8(PyObject_Str(value)));
        PyErr_SetString(PyExc_TypeError, error_msg);
        return 0;
      }
    }
  }
  return 1;
}

void PySchema_PrintAnnotations(PyObject *obj) {
  PyObject *annotations = PySchema_GetAnnotations(obj);
  if (annotations == NULL) {
    return;
  }
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str =
        PyObject_GenericGetAttr(value, PyUnicode_FromString("__name__"));
    char key_str_c[100];
    char value_str_c[100];
    sprintf(key_str_c, "%s", PyUnicode_AsUTF8(key_str));
    sprintf(value_str_c, "%s", PyUnicode_AsUTF8(value_str));
    printf("key: %s, value: %s\n", key_str_c, value_str_c);
    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
}

void PySchema_PrintDir(PyObject *obj) {
  PyObject *dir = PyObject_Dir(obj);
  if (dir == NULL) {
    return;
  }
  Py_ssize_t len = PyList_Size(dir);
  for (Py_ssize_t i = 0; i < len; i++) {
    PyObject *attr = PyList_GetItem(dir, i);
    PyObject *attr_str = PyObject_Str(attr);
    char attr_str_c[100];
    sprintf(attr_str_c, "%s", PyUnicode_AsUTF8(attr_str));
    fprintf(stderr, "attr: %s\n", attr_str_c);
    Py_DECREF(attr_str);
  }
  Py_DECREF(dir);
}

void PySchema_PrintTypeDict(PyTypeObject *type) {
  PyObject *dict = type->tp_dict;
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  // print type __name__
  PyObject *type_name = PyObject_GetName((PyObject *)type);
  fprintf(stderr, "Type: %s\n", PyUnicode_AsUTF8(type_name));
  Py_DECREF(type_name);
  while (PyDict_Next(dict, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str = PyObject_Str(value);
    char key_str_c[100];
    char value_str_c[100];
    sprintf(key_str_c, "%s", PyUnicode_AsUTF8(key_str));

    sprintf(value_str_c, "%s", PyUnicode_AsUTF8(value_str));
    fprintf(stderr, "key: %s, value: %s\n", key_str_c, value_str_c);
    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
}