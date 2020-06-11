FROM python:3.7-slim-buster

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH="${PATH}:/root/.poetry/bin"

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY Makefile pyproject.toml ./

RUN make download-poetry && \
    poetry lock -n && \
    poetry install -n

COPY . .
