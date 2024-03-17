# Use an official Python runtime as a parent image.
# See https://hub.docker.com/_/python for more information.
# To understand docker image tags, see https://forums.docker.com/t/differences-between-standard-docker-images-and-alpine-slim-versions/134973
FROM python:alpine

# Install system packages
RUN apk update \
    && apk add --no-cache \
    # deps for downloading models
    curl \
    # deps for development
    git \
    openssh-client \
    # deps for python packages
    build-base \
    python3-dev


# Set the working directory to /opt/app
WORKDIR /opt/app

# Upgrade pip
RUN pip install --upgrade pip

# Install UV
# To learn more about UV, see https://github.com/astral-sh/uv
RUN pip install uv

# Copy the installation script
COPY install_dependencies.sh .

# Change the permissions of the installation script to make it executable
RUN chmod +x ./install_dependencies.sh

# Copy the requirements file
COPY requirements.txt .

# Install dependencies from the requirements file
RUN ./install_dependencies.sh ./requirements.txt
