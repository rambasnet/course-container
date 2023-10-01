all: check-style check-types test run clean

test:
	pytest test_cold.py
	pytest test_unit_cold.py
	
run:
	@cat data/1.in | python cold.py | diff - data/1.ans
	@cat data/2.in | python cold.py | diff - data/2.ans
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