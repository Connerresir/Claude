#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/app
python -m unittest discover -s .
