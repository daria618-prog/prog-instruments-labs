lint:
	ruff check python

format-check:
	ruff format --check python

format:
	ruff format python

type-check:
	pyright python

fullcheck: lint format-check type-check

fix:
	ruff check python --fix

test:
	pytest python/test_gilded_rose.py

run:
	python python/texttest_fixture.py

precommit:
	pre-commit install
	pre-commit install --hook-type pre-push