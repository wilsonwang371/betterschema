#ifndef __DEBUG_H
#define __DEBUG_H

#include <stdio.h>

#define MAX_STACK_LEVELS 50
#define UNUSED(x) (void)(x)

#define LOG_LEVEL_DEBUG 3
#define LOG_LEVEL_INFO 2
#define LOG_LEVEL_WARN 1
#define LOG_LEVEL_FATAL 0

#define LOG_LEVEL LOG_LEVEL_DEBUG

#define PANIC(fmt, ...)                                                        \
  do {                                                                         \
    fprintf(stderr, "\033[1;31m");                                             \
    fprintf(stderr, "Panic: %s:%d: ", __FILE__, __LINE__);                     \
    fprintf(stderr, fmt, ##__VA_ARGS__);                                       \
    fprintf(stderr, "\033[0m");                                                \
    print_stacktrace();                                                        \
    exit(1);                                                                   \
  } while (0)

#define FATAL(fmt, ...)                                                        \
  do {                                                                         \
    if (LOG_LEVEL >= 0) {                                                      \
      break;                                                                   \
    }                                                                          \
    fprintf(stderr, "\033[1;31m");                                             \
    fprintf(stderr, "Fatal: %s:%d: ", __FILE__, __LINE__);                     \
    fprintf(stderr, fmt, ##__VA_ARGS__);                                       \
    fprintf(stderr, "\033[0m");                                                \
    exit(1);                                                                   \
  } while (0)

#define WARN(fmt, ...)                                                         \
  do {                                                                         \
    if (LOG_LEVEL >= 1) {                                                      \
      break;                                                                   \
    }                                                                          \
    fprintf(stderr, "\033[1;33m");                                             \
    fprintf(stderr, "Warning: %s:%d: ", __FILE__, __LINE__);                   \
    fprintf(stderr, fmt, ##__VA_ARGS__);                                       \
    fprintf(stderr, "\033[0m");                                                \
  } while (0)

#define INFO(fmt, ...)                                                         \
  do {                                                                         \
    if (LOG_LEVEL >= 2) {                                                      \
      break;                                                                   \
    }                                                                          \
    fprintf(stderr, "\033[1;32m");                                             \
    fprintf(stderr, "Info: %s:%d: ", __FILE__, __LINE__);                      \
    fprintf(stderr, fmt, ##__VA_ARGS__);                                       \
    fprintf(stderr, "\033[0m");                                                \
  } while (0)

#define DEBUG(fmt, ...)                                                        \
  do {                                                                         \
    if (LOG_LEVEL >= 3) {                                                      \
      break;                                                                   \
    }                                                                          \
    fprintf(stderr, "\033[1;34m");                                             \
    fprintf(stderr, "Debug: %s:%d: ", __FILE__, __LINE__);                     \
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
