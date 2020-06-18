IMAGE := bitcoinql
VERSION := latest

build-docker:
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f Dockerfile

run-docker:
	docker run \
		-it \
		-v $(PWD):/app \
		$(IMAGE):$(VERSION) \
		/bin/bash

clean-docker:
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: build-docker clean-docker run-docker


