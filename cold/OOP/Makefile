all: check-style check-types test run clean

test:
	pytest --verbose --color=yes test_solution.py
	pytest --verbose --color=yes test_temperature.py

run:
	@cat ../data/1.in | python cold_oop.py | diff - ../data/1.ans
	@cat ../data/2.in | python cold_oop.py | diff - ../data/2.ans
	@echo "All kattis sample test data test done..."

check-types:
	mypy --disallow-untyped-defs --strict cold_oop.py
	mypy --disallow-untyped-defs --strict temperature.py
	mypy --disallow-untyped-defs --strict test_solution.py
	mypy --disallow-untyped-defs --strict test_temperature.py

check-style:
	flake8 cold_oop.py
	flake8 temperature.py
	flake8 test_solution.py
	flake8 test_temperature.py

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache