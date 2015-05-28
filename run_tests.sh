#!/bin/bash

python -m unittest discover -s test/lexer -p '*_test.py'
python -m unittest discover -s test/parser -p '*_test.py'
python -m unittest discover -s test/types -p '*_test.py'
python -m unittest discover -s test/interpreter -p '*_test.py'
python -m unittest discover -s test/e2e -p '*_test.py'
