#!/bin/bash

# fail if black is not installed
if ! [ -x "$(command -v black)" ]; then
  echo 'Error: black is not installed.' >&2
  exit 1
fi

# Format all python code
black .
