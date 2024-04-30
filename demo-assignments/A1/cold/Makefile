.PHONY: all
all: check-style check-types run-test clean
	@echo "All done!"

.PHONY: run-test
run-test:
	pytest --verbose --color=yes --cov --cov-report term --cov-report html tests/

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

