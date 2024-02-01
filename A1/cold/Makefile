all: check-style check-types run-test clean

.PHONY: test
run-test:
	pytest --verbose --color=yes --cov  tests --cov-report term-missing --cov-report html

.PHONY: check-types
check-types:
	mypy --disallow-untyped-defs --strict .

.PHONY: check-style
check-style:
	flake8 .

.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .

.PHONY: clean
clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`

