# provide path to where plantuml.jar is downloaded
PLANTUML = java -jar ~/plantuml.jar
DOCS = docs
PROBLEM = hello
PYTHON = python3

.PHONY: all
all: check-style fix-style check-types run-test create-docs create-uml
	@echo "All done!"

.PHONY: run-test
run-test:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	pytest --verbose --color=yes --cov --cov-report term --cov-report html tests/
	@echo "All unittests passed!"

.PHONY: check-types
check-types:
# use shell command which to check if mypy is installed and is in $PATH
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict .
	@echo "Type checking done."

.PHONY: create-doc-folder
create-doc-folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

.PHONY: create-docs
create-docs: create-doc-folder
	pdoc -o ./docs main.py hello.py # creates .md docs inside docs
	@echo "html docs created and saved in $(DOCS)"

.PHONY: create-uml
create-uml: create-doc-folder
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ~/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
endif
	$(PLANTUML) uml/HelloWorld.plantuml
	$(PLANTUML) uml/Main.plantuml
	$(PLANTUML) uml/solution.plantuml
	@echo "UML diagrams created and saved in uml folder"

.PHONY: check-style
check-style:
	flake8 .

.PHONY: fix-style
fix-style:
	autopep8 --in-place --recursive --aggressive --aggressive .
