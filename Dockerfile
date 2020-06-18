FROM python:3.8-slim-buster

WORKDIR /app

COPY setup.py pyproject.toml ./

RUN /opt/bb/bin/python3.8 -m pip install -e .

COPY . .
