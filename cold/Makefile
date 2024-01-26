all: check-style check-types test run clean

test:
	pytest test_cold.py
	pytest test_unit_cold.py
	
run:
	@kattis test
	@echo "All kattis sample test data test done..."

check-types:
	mypy --disallow-untyped-defs --strict cold.py
	mypy --disallow-untyped-defs --strict test_cold.py
	mypy --disallow-untyped-defs --strict test_unit_cold.py

check-style:
	flake8 cold.py
	flake8 test_cold.py
	flake8 test_unit_cold.py

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	