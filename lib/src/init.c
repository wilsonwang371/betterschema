#include "init.h"
#include "utils.h"

int schema_init(PyObject *self, PyObject *args, PyObject *kwds) {

  // get annotations
  PyObject *annotations = schema_annotations(self);
  if (annotations == NULL) {
    return -1;
  }

  // get the number of arguments
  Py_ssize_t num_args = PyTuple_Size(args);
  if (num_args != 1) {
    PyErr_SetString(PyExc_TypeError, "Expected 1 argument");
    return -1;
  }

  // get first argument and check if it is a dict
  PyObject *arg = PyTuple_GetItem(args, 0);
  if (!PyDict_Check(arg)) {
    PyErr_SetString(PyExc_TypeError, "Expected dict");
    return -1;
  }

  // iterate all dict items
  PyObject *key, *value;
  Py_ssize_t pos = 0;
  while (PyDict_Next(arg, &pos, &key, &value)) {
    PyObject *key_str = PyObject_Str(key);

    // make sure the key is also inside the annotations
    if (!schema_contains_annotation(self, PyUnicode_AsUTF8(key_str))) {
      char error_msg[100];
      sprintf(error_msg, "Attribute \"%s\" not found in annotations",
              PyUnicode_AsUTF8(key_str));
      PyErr_SetString(PyExc_AttributeError, error_msg);
      return -1;
    }

    // make sure the value type matches the annotation type
    AnnotationDataType attr_type =
        schema_annotation_type(self, PyUnicode_AsUTF8(key_str));
    // get the object type from the value object
    PyObject *value_type = PyObject_Type(value);
    const char *value_type_name = object_name_cstr(value_type);
    AnnotationDataType value_type_enum = str_to_typevalue(value_type_name);
    if (attr_type != value_type_enum) {
      char error_msg[100];
      sprintf(error_msg, "Expected %s, got %s", typevalue_to_str(attr_type),
              value_type_name);
      PyErr_SetString(PyExc_TypeError, error_msg);
      return -1;
    }

    if (PyObject_GenericSetAttr(self, key, value) < 0) {
      return -1;
    }

    Py_DECREF(key_str);
  }

  // TODO: update this

  // iterate all annotations
  //   PyObject *key, *value;
  //   Py_ssize_t pos = 0;
  //   while (PyDict_Next(annotations, &pos, &key, &value)) {
  //     PyObject *key_str = PyObject_Str(key);
  //     PyObject *value_str = PyObject_Str(value);
  //     char key_str_c[100];
  //     char value_str_c[100];
  //     sprintf(key_str_c, "%s", PyUnicode_AsUTF8(key_str));
  //     sprintf(value_str_c, "%s", PyUnicode_AsUTF8(value_str));
  //     fprintf(stderr, "key: %s, value: %s\n", key_str_c, value_str_c);
  //     Py_DECREF(key_str);
  //     Py_DECREF(value_str);
  //   }

  UNUSED(args);
  UNUSED(kwds);
  fprintf(stderr, "schema_init\n");
  return 0;
}
