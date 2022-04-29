# Pull base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_VERSION_CHECK=on

# System dependencies:
RUN pip install poetry

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry install

# Creating folders and files for project:
COPY . /code/
