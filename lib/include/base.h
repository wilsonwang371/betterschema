#ifndef _BASE_H
#define _BASE_H

#define UNUSED(x) (void)(x)

// Type values
typedef enum {
  TYPE_INT,
  TYPE_FLOAT,
  TYPE_STR,
  TYPE_BOOL,
  TYPE_UNKNOWN
} AnnotationDataType;

AnnotationDataType PySchema_ConvertStrToAnnoType(const char *str);
const char *PySchema_ConvertAnnoTypeToStr(AnnotationDataType type);

#endif // _BASE_H
