MAKEFLAGS += --silent

# Automatically activate virtual environment in ./venv for all targets
VENV = ../venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

# Set hash seed for exact reproducability
export PYTHONHASHSEED = 569895214

CODE = RSA
DOCS = docs
TESTS = tests

GIT ?= git
PIP ?= pip
PYCODESTYLE ?= ${VIRTUAL_ENV}/bin/pycodestyle
PYDOCSTYLE ?= ${VIRTUAL_ENV}/bin/pydocstyle
PYLINT ?= ${VIRTUAL_ENV}/bin/pylint
PYTHON ?= python
PYTEST ?= ${VIRTUAL_ENV}/bin/pytest

.PHONY: all nightly setup clean build test test-extended doc docs \
        lint lint-warnings lint-errors lint-reports style package

all: clean build #test docs

nightly: clean setup build test-extended docs

setup:
	$(PIP) install -r requirements.txt -q

clean:
	$(PYTHON) setup.py clean
	rm -rf build
	rm -rf crasecli.egg-info
	rm -rf dist
	rm -rf docs/_build
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '.coverage*' -exec rm -f {} +

build:
	$(PIP) install -e . | grep -v 'Requirement already satisfied'

test: build style
	$(PYTEST) $(TESTS) -m "not extended" --cov-report term-missing --cov $(CODE)

test-extended: build style
	$(PYTEST) $(TESTS) --cov-report term-missing --cov $(CODE)

doc: docs

docs: build
	$(MAKE) -C $(DOCS) html

lint:
	$(PYLINT) $(CODE)

lint-warnings:
	$(PYLINT) $(CODE) -d C,R

lint-errors:
	$(PYLINT) $(CODE) -d C,R,W

lint-reports:
	$(PYLINT) $(CODE) --reports=yes

style: lint
	$(PYCODESTYLE) $(CODE) $(TESTS) --config=setup.cfg
	$(PYDOCSTYLE) $(CODE)

package: all
	$(PYTHON) setup.py bdist_wheel
	$(PYTHON) setup.py bdist_egg
