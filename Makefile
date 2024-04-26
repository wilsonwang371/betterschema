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

test: build
	PYTHONPATH=$(LIB_BUILD_DIR) python -m unittest $(PROJECT_DIR)/tests/*.py

clean:
	rm -rf $(PROJECT_DIR)/build
	rm -rf $(PROJECT_DIR)/dist
	rm -rf $(PROJECT_DIR)/.eggs
	rm -rf $(PROJECT_DIR)/__pycache__
	rm -rf $(PROJECT_DIR)/*.egg-info

# build wheel using pip
build: clean
	python -m build --wheel --sdist
