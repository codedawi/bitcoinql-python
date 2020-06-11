SHELL := /usr/bin/env bash
IMAGE := bitcoinql
VERSION := latest

.PHONY: download-poetry
download-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

.PHONY: docker
docker:
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f Dockerfile --no-cache

.PHONY: clean_docker
clean_docker:
	docker rmi -f $(IMAGE):$(VERSION)

