#!/bin/bash

# Check if the path to the requirements file was provided
if [ -z "$1" ]; then
    echo "Please provide the path to the requirements file"
    exit 1
fi

# Set the path of the requirements.txt file
REQUIREMENTS_FILE=$1

# Initialize the virtual environment
uv venv

# Activate the virtual environment
source venv/bin/activate

# Install the Python packages
uv pip install -r requirements.txt
