TEST = pytest 
TEST_ARGS = -v
TYPE_CHECK = mypy --strict
STYLE_CHECK = flake8

.PHONY: all
all: test clean

# discover and run all tests
.PHONY: test
test:
	$(TEST) $(TEST_ARGS) .

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache

.PHONY: push
push: test clean
	