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

PyObject *object_name_obj(PyObject *obj) {
  return PyObject_GenericGetAttr(obj, PyUnicode_FromString("__name__"));
}

const char *object_name_cstr(PyObject *obj) {
  PyObject *name = object_name_obj(obj);
  if (name == NULL) {
    PyErr_SetString(PyExc_AttributeError, "__name__ not found");
    return NULL;
  }
  return PyUnicode_AsUTF8(name);
}

PyObject *schema_annotations(PyObject *obj) {
  PyTypeObject *type;
  if (PyType_Check(obj) == 0) {
    type = Py_TYPE(obj);
  } else {
    type = (PyTypeObject *)obj;
  }
  PyObject *annotations =
      PyDict_GetItemString(type->tp_dict, "__annotations__");
  if (annotations == NULL) {
    fprintf(stderr, "__annotations__ not found\n");
    PyErr_SetString(PyExc_AttributeError, "__annotations__ not found");
    return NULL;
  } else {
    if (!is_valid_annotations(annotations)) {
      fprintf(stderr, "Invalid annotations\n");
      return NULL;
    }
  }

  return annotations;
}

int schema_contains_annotation(PyObject *obj, const char *attr) {
  PyObject *annotations = schema_annotations(obj);
  if (annotations == NULL) {
    fprintf(stderr, "Failed to get annotations while checking annotation\n");
    return 0;
  }
  PyObject *attr_str = PyUnicode_FromString(attr);
  int has_attr = PyDict_Contains(annotations, attr_str);
  Py_DECREF(attr_str);
  return has_attr;
}

AnnotationDataType schema_annotation_type(PyObject *obj, const char *attr) {
  AnnotationDataType result = TYPE_UNKNOWN;
  PyObject *annotations = schema_annotations(obj);
  if (annotations == NULL) {
    fprintf(stderr,
            "Failed to get annotations while getting annotation type\n");
    assert(0);
  }

  PyObject *typeval = PyDict_GetItemString(annotations, attr);
  if (typeval == NULL) {
    fprintf(stderr, "Failed to get type\n");
    return TYPE_UNKNOWN;
  }
  if (PyType_Check(typeval) == 0) {
    fprintf(stderr, "Failed to get type\n");
    return TYPE_UNKNOWN;
  }

  // get type name
  const char *type_name = object_name_cstr((PyObject *)typeval);
  if (type_name == NULL) {
    fprintf(stderr, "Failed to get type name\n");
    return TYPE_UNKNOWN;
  }

  result = type_str_to_val(type_name);
  Py_DECREF(typeval);
  return result;
}

int is_valid_annotations(PyObject *annotations) {
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  char error_msg[100];
  while (PyDict_Next(annotations, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);
    PyObject *value_str = object_name_obj(value);

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

    Py_DECREF(key_str);
    Py_DECREF(value_str);
  }
  return 1;
}

void print_schema_annotations(PyObject *obj) {
  PyObject *annotations = schema_annotations(obj);
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

void print_schema_attributes(PyObject *obj) {
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

void print_schema_dir(PyObject *obj) {
  PyObject *dir = PyObject_Dir(obj);
  if (dir == NULL) {
    fprintf(stderr, "Failed to get dir\n");
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

void print_type_dict(PyTypeObject *type) {
  PyObject *dict = type->tp_dict;
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  // print type __name__
  PyObject *type_name = object_name_obj((PyObject *)type);
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