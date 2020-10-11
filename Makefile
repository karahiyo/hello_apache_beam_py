SHELL := /usr/local/bin/fish
PYTHON := python3

setup:
	$(PYTHON) -m venv venv

install:
	pip install -r requirements.txt

