#!/usr/bin/env bash

rm -rf dist/*
./venv/bin/pip install wheel
./venv/bin/python setup.py sdist bdist_wheel