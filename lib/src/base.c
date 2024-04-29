#include "base.h"
#include "string.h"

// Convert a type string to a type value
AnnotationDataType PySchema_ConvertStrToAnnoType(const char *str) {
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

const char *PySchema_ConvertAnnoTypeToStr(AnnotationDataType type) {
  switch (type) {
  case TYPE_INT:
    return "int";
  case TYPE_FLOAT:
    return "float";
  case TYPE_STR:
    return "str";
  case TYPE_BOOL:
    return "bool";
  case TYPE_UNKNOWN:
    return "unknown";
  }
}
