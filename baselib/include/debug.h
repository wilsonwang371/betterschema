#ifndef __DEBUG_H
#define __DEBUG_H

#include <stdio.h>

#define MAX_STACK_LEVELS 50
#define UNUSED(x) (void)(x)

#define FATAL(fmt, ...)                                                        \
  do {                                                                         \
    fprintf(stderr, "\033[1;31m");                                             \
    fprintf(stderr, "Fatal: %s:%d: ", __FILE__, __LINE__);                     \
    fprintf(stderr, fmt, ##__VA_ARGS__);                                       \
    fprintf(stderr, "\033[0m");                                                \
    exit(1);                                                                   \
  } while (0)

#define WARN(fmt, ...)                                                         \
  do {                                                                         \
    fprintf(stderr, "\033[1;33m");                                             \
    fprintf(stderr, "Warning: %s:%d: ", __FILE__, __LINE__);                   \
    fprintf(stderr, fmt, ##__VA_ARGS__);                                       \
    fprintf(stderr, "\033[0m");                                                \
  } while (0)

// only on macos
#if defined(__APPLE__) && defined(__MACH__)
#include <execinfo.h>

inline void print_stacktrace() {
  void *buffer[MAX_STACK_LEVELS];
  int levels = backtrace(buffer, MAX_STACK_LEVELS);
  backtrace_symbols_fd(buffer + 1, levels - 1, 2);
}
#else
inline void print_stacktrace() {
  WARN("Stack trace not supported on Windows\n");
}
#endif // !defined(_WIN32) && !defined(_WIN64)

#endif // __DEBUG_H
