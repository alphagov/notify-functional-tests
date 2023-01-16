.DEFAULT_GOAL := help
SHELL := /bin/bash

NOTIFY_CREDENTIALS ?= ~/.notify-credentials

.PHONY: help
help:
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: bootstrap
bootstrap: ## Install build dependencies
	mkdir -p logs screenshots
	pip install -r requirements.txt

.PHONY: clean
clean: ## Remove temporary files
	rm -rf screenshots/*
	rm -rf logs/*

.PHONY: test
test: clean ## Run functional tests against local environment
	isort --check-only tests
	flake8 .
	black --check .
	pytest -v tests/functional/preview_and_dev -n auto --dist loadgroup
	pytest -v tests/document_download/preview_and_dev

.PHONY: generate-staging-db-fixtures
generate-staging-db-fixtures: ## Generates DB fixtures for the staging database
	$(if $(shell which gpg2), $(eval export GPG=gpg2), $(eval export GPG=gpg))
	$(if ${GPG_PASSPHRASE_TXT}, $(eval export DECRYPT_CMD=echo -n $$$${GPG_PASSPHRASE_TXT} | ${GPG} --quiet --batch --passphrase-fd 0 --pinentry-mode loopback -d), $(eval export DECRYPT_CMD=${GPG} --quiet --batch -d))

	@jinja2 --strict db_fixtures/staging.sql.j2 \
	    --format=json \
	    -o db_fixtures/staging.sql \
	    <(${DECRYPT_CMD} ${NOTIFY_CREDENTIALS}/credentials/functional-tests/staging-functional-db-fixtures.gpg) 2>&1
