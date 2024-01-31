TEST = python -m pytest 
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive

.PHONY: all
all: check-style check-type run-test clean

.PHONY: check-type
check-type:
	$(TYPE_CHECK) hello
	$(TYPE_CHECK) cold

.PHONY: check-style
check-style:
	$(STYLE_CHECK) hello
	$(STYLE_CHECK) cold

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) hello
	$(TEST) $(TEST_ARGS) cold

.PHONY: fix-style
fix-style:
	$(STYLE_FIX) hello
	$(STYLE_FIX) cold

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -type d -name .coverage` # remove all coverage cache 
	