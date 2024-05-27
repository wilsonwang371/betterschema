#include "utils.h"
#include "init.h"
#include "schema.h"
#include "schematypes.h"

// Get the current thread frame global and local
int PySys_GetGlobalLocal(PyObject **pGlobal, PyObject **pLocal) {
  // Access the global and local dictionaries
  *pGlobal = PyEval_GetGlobals();
  *pLocal = PyEval_GetLocals();
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

PyObject *PySchema_SetAnnoListObj(PyObject *obj, PyObject *annotations) {
  PyTypeObject *type;
  if (PyType_Check(obj) == 0) {
    type = Py_TYPE(obj);
  } else {
    // type object
    type = (PyTypeObject *)obj;
  }
  if (type == NULL) {
    WARN("Failed to get type in set annotations\n");
    return NULL;
  }

  if (PyDict_SetItemString(type->tp_dict, "__annotations__", annotations) ==
      -1) {
    PyErr_SetString(PyExc_RuntimeError, "Failed to set annotations");
    return NULL;
  }

  return annotations;
}

PyObject *PySchema_GetAnnoListObj(PyObject *obj) {
  PyTypeObject *type;
  if (PyType_Check(obj) == 0) {
    type = Py_TYPE(obj);
  } else {
    // type object
    type = (PyTypeObject *)obj;
  }
  if (type == NULL) {
    WARN("Failed to get type in get annotations\n");
    return NULL;
  }

  PyObject *annotations =
      PyDict_GetItemString(type->tp_dict, "__annotations__");
  if (annotations == NULL) {
    PyErr_SetString(PyExc_AttributeError, "__annotations__ not found");
    return NULL;
  } else {
    if (!PySchema_IsValidAnnotations(annotations)) {
      WARN("Invalid annotations\n");
      return NULL;
    }
  }

  return annotations;
}

int PySchema_IsOptionalAnno_ByCStr(PyObject *obj, const char *attr) {
  PyObject *typeval = PySchema_GetAnnoObj_ByCStr(obj, attr);
  if (typeval == NULL) {
    WARN("Failed to get type while getting item %s\n", attr);
    return 0;
  }
  SchemaType type = PySchema_ToSchemaType_FromTypeObj(typeval);
  if (type == TypeOptional) {
    return 1;
  }
  return 0;
}

PyObject *PySchema_GetAnnoObj_ByCStr(PyObject *obj, const char *attr) {
  PyObject *annotations = PySchema_GetAnnoListObj(obj);
  if (annotations == NULL) {
    WARN("Failed to get annotations while getting annotation obj\n");
    return NULL;
  }

  PyObject *typeval = PyDict_GetItemString(annotations, attr);
  if (typeval == NULL) {
    return NULL;
  }
  return typeval;
}

int PySchema_ContainAnnoObj_ByCStr(PyObject *obj, const char *attr) {
  return PySchema_GetAnnoObj_ByCStr(obj, attr) != NULL;
}

// TODO: remove this?
PyObject *PySchema_GetAnnotationType(PyObject *obj, const char *attr) {
  PyObject *typeval = PySchema_GetAnnoObj_ByCStr(obj, attr);
  if (typeval == NULL) {
    WARN("Failed to get type while getting item %s\n", attr);
    return NULL;
  }
  if (PyType_Check(typeval) != 0) {
    // basic type
    return typeval;
  }
  // Union type returns 0 in case of isinstance(var, type)
  // check if it is a type.GenericAlias
  // or _UnionGenericAlias
  if (strcmp(Py_TYPE(typeval)->tp_name, "types.GenericAlias") == 0) {
    PyObject *origin = PyObject_GetAttrString(typeval, "__origin__");
    if (PyType_Check(origin) == 0) {
      WARN("Failed to get origin in anno type\n");
      return NULL;
    }
    // if it is a list or dict type, return typeval
    if ((PyTypeObject *)origin == &PyList_Type ||
        (PyTypeObject *)origin == &PyDict_Type) {
      return origin;
    }
  } else if (strcmp(Py_TYPE(typeval)->tp_name, "_UnionGenericAlias") == 0) {
    PyObject *args = PyObject_GetAttrString(typeval, "__args__");
    if (args == NULL) {
      WARN("Failed to get args\n");
      return NULL;
    }
    // make sure it is a tuple
    if (!PyTuple_Check(args)) {
      WARN("Expected tuple\n");
      return NULL;
    }

    // make sure the second element is None
    PyObject *second_element = PyTuple_GetItem(args, 1);
    if (second_element == NULL) {
      WARN("Failed to get second element\n");
      return NULL;
    }

    // return the first element
    return PyTuple_GetItem(args, 0);
  }
  return NULL;
}

int PySchema_IsValidAnnotations(PyObject *annotations) {
  PyObject *key, *value;
  PyObject *schema = PySchema_GetRegisteredSchemaDictObj();
  Py_ssize_t pos = 0;

  if (schema == NULL) {
    return 0;
  }

  while (PyDict_Next(annotations, &pos, &key, &value)) {
    // print key and value
    int res = PySchema_IsValidTypeObj(value);
    if (res == 0) {
      PyErr_SetString(
          PyExc_TypeError,
          sprintf_static("Invalid type %s", PyObject_GetNameStr(value)));
      return 0;
    }
  }

  return 1;
}

void PySchema_PrintAnnotations(PyObject *obj) {
  PyObject *annotations = PySchema_GetAnnoListObj(obj);
  if (annotations == NULL) {
    return;
  }
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str =
        PyObject_GenericGetAttr(value, PyUnicode_FromString("__name__"));
    WARN("key: %s, value: %s\n", PyUnicode_AsUTF8(key_str),
         PyUnicode_AsUTF8(value_str));
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
    WARN("attr: %s\n", PyUnicode_AsUTF8(attr_str));
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
  WARN("Type: %s\n", PyUnicode_AsUTF8(type_name));
  Py_DECREF(type_name);
  while (PyDict_Next(dict, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str = PyObject_Str(value);
    WARN("key: %s, value: %s\n", PyUnicode_AsUTF8(key_str),
         PyUnicode_AsUTF8(value_str));
    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
}

const char *sprintf_static(const char *fmt, ...) {
  static char buffer[1 << 10];
  va_list args;
  va_start(args, fmt);
  vsprintf(buffer, fmt, args);
  va_end(args);
  return buffer;
}