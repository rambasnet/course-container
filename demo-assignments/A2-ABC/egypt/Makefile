PLANTUML = java -jar ~/plantuml.jar

all: check-style check_types unittest create-uml localtest


.PHONY: check-style
check-style:
	flake8 .
	@echo "Code style check done."

.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .
	
.PHONY: check_types
check-types:
	mypy --disallow-untyped-defs --strict .
	@echo "Static type check done."

.PHONY: unittest
unittest:
	pytest --verbose  --color=yes --cov --cov-report term --cov-report html tests/
	@echo "Unittest done."

.PHONY: create-uml
create-uml:
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ~/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
endif
	$(PLANTUML) uml/abc.plantuml
	$(PLANTUML) uml/interaction.plantuml
	$(PLANTUML) uml/solution.plantuml
	$(PLANTUML) uml/triangle.plantuml
	@echo "UML diagrams created and saved in uml folder"

.PHONY: cleanall
localtest:
	kattis test -m egypt_abc.py
	kattis test -m egypt_singleton.py
	@echo "Local kattis sample data test done."


.PHONY: clean
clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type f -name .coverage`

