#!/bin/bash

# Update pip in the virtual environment
/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip

pip install -r requirements.txt
# Run your Flask application
/opt/render/project/src/.venv/bin/python main_server.py
