#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd)"

function format_python_code() {
    echo "Formatting Python code"

    # fail if isort is not installed
    if ! [ -x "$(command -v isort)" ]; then
        echo 'Error: isort is not installed.' >&2
        exit 1
    fi

    # fail if black is not installed
    if ! [ -x "$(command -v black)" ]; then
        echo 'Error: black is not installed.' >&2
        exit 1
    fi


    isort **/*.py

    # Format all python code
    black $PROJECT_DIR
}

function format_c_code() {
    echo "Formatting C code"
    # fail if clang-format is not installed
    if ! [ -x "$(command -v clang-format)" ]; then
        echo 'Error: clang-format is not installed.' >&2
        exit 1
    fi

    # Format all C code
    FILES=$(find $PROJECT_DIR -name '*.c' -o -name '*.h')
    for file in $FILES; do
        clang-format -i $file
    done
}

format_python_code
format_c_code
