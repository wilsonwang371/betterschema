# get project dir
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# find lib.* directory
LIB_BUILD_DIR := $(shell find $(PROJECT_DIR)/build -type d -name "lib.*")

.PHONY: format test clean

# default target 
all: format build

# format all python files
format:
	$(PROJECT_DIR)/scripts/format.sh

test: build-wheel
	PYTHONPATH=$(LIB_BUILD_DIR) python -m unittest $(PROJECT_DIR)/tests/test*.py

clean:
	rm -rf $(PROJECT_DIR)/build
	rm -rf $(PROJECT_DIR)/dist
	rm -rf $(PROJECT_DIR)/.eggs
	find $(PROJECT_DIR) -type d -name "__pycache__" -exec rm -rf {} +
	find $(PROJECT_DIR) -type d -name "*.egg-info" -exec rm -rf {} +

# build wheel using pip
build: clean
	python -m build --sdist

build-wheel: clean
	python -m build --wheel

install: build
	python3 -m pip install $(PROJECT_DIR)/dist/*.whl
