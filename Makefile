TEST = pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = python -m pytest
ASSIGNMENT = ./assignments

.PHONY: all
all: check-style check-type run-test-coverage clean
	@echo "All checks passed"

.PHONY: check-type
check-type:
	@echo "FIXME"

.PHONY: check-style
check-style:
	@echo "FIXME"

# discover and run all tests
.PHONY: run-test
run-test:
	@echo "FIXME"

.PHONY: run-test-coverage
run-test-coverage:
	@echo "FIXME"

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
