# get project dir
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: format test clean

# format all python files
format:
	$(PROJECT_DIR)/scripts/format.sh

test: clean
	PYTHONPATH=$(PROJECT_DIR)/src python -m unittest 

clean:
	rm -rf $(PROJECT_DIR)/build
	rm -rf $(PROJECT_DIR)/dist
	rm -rf $(PROJECT_DIR)/.eggs
	rm -rf $(PROJECT_DIR)/__pycache__
	rm -rf $(PROJECT_DIR)/*.egg-info

# build wheel using pip
build: clean
	python -m build --wheel --sdist
