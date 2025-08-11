.PHONY: test lint

test:
	pytest -n 10

lint:
	ruff check --fix .
	ruff format .
