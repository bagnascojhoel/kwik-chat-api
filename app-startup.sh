#!/bin/bash
export FLASK_APP=./src/main.py

pipenv run flask --debug run -h localhost