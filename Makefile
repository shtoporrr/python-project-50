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
	flake8 gendiff

test:
	uv pip install pytest
	pytest

test-coverage:
	uv pip install pytest-cov
	pytest --cov=gendiff --cov-report xml

.PHONY: install test lint selfcheck check build