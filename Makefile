install:
	uv pip install --editable .

build:
	python -m build

publish:
	twine check dist/*

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	uv pip install flake8
	.venv/bin/flake8 gendiff

test:
	uv pip install pytest
	.venv/bin/pytest

test-coverage:
	uv pip install pytest-cov
	.venv/bin/pytest --cov=gendiff --cov-report xml

.PHONY: install test lint selfcheck check build