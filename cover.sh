#!/usr/bin/bash

PYTHONROOT=/usr/bin PYTHONPATH=./src:./utests coverage run -m pytest -k test_ -v .

coverage report
coverage xml
coverage html

