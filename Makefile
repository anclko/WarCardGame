# ---------------------------------------------------------
# Setup a venv and install packages.
#

run:
	python main.py

# Setup a venv and install #
venv:
	python -m venv .venv
## In the terminal:
## FOR WINDOWS: . .venv/Scripts/activate
## FOR MAC/LINUX: . .venv/bin/activate



## Check version
version: check-virtual-env
	@printf "Python executable version: "
	@$(PYTHON) --version



check-virtual-env:
		@echo virtual-env: $${VIRTUAL_ENV?"Please source your .venv/"}



## Instals pip packages based on package list in requirements.txt
install: check-virtual-env
		pip install -r requirements.txt
		$(PYTHON) -m pip install --upgrade -q pip



## Display pip packages
installed: check-virtual-env
		$(PYTHON) -m pip list



## pylint coverage
pylint: check-virtual-env
		@for py in source/*.py; do echo "Linting $$py"; pylint -d C0103 -rn $$py; done
		@for py in source/*/*.py; do echo "Linting $$py"; pylint -d C0103 -rn $$py; done
		@for py in source/*/*/*.py; do echo "Linting $$py"; pylint -d C0103 -rn $$py; done



## flake8 coverage
flake8: check-virtual-env
		@$(call MESSAGE,$@)
		-flake8 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg,$(VENV),venv,*.pyc



## Check pylint and flake8 coverage
lint: check-virtual-env 
		$(MAKE) pylint
		$(MAKE) flake8



## Clear temporary interpeter cache and virtual environment files
clean:
		rm -rf source/__pycache__
		rm -rf source/*/__pycache__
		rm -rf source/*/*/__pycache__
		rm -rf source/*/*/*/__pycache__
		rm -rf source/*.pyc
		rm -rf source/*/*.pyc
		rm -rf source/*/*/*.pyc
		rm -rf source/*/*/*/*.pyc
		rm -rf $(VENV)



## Clears documentation files
clean-doc:
		rm -rf ./doc



## Clear coverage files
clean-cov:
		rm -rf htmlcov



## Clear all generated files
clean-all: clean clean-doc clean-cov



## Generate documentation in an HTML file using pdoc
pdoc: check-virtual-env
		@$(call message, $@)
		pdoc -o doc/api ./source/*.py ./source/*/*.py ./source/*/*/*.py



## Open documentation's index html file in browser
pdoc-html: check-virtual-env
	@(\
		if [[ $(USER_OS) == "WINDOWS" ]]; then \
			start doc/api/index.html & \
		elif [[ $(USER_OS) == "DARWIN" ]]; then	\
			open doc/api/index.html &	\
		elif [[ $(USER_OS) == "LINUX" ]]; then	\
			xdg-open doc/api/index.html & \
		fi	\
	)



## Converting UML diagrams from code
uml-png: check-virtual-env
		@$(call message, $@)
		install -d doc/uml
		pyreverse ./source/*.py
		pyreverse ./source/src/*.py ./source/test/*.py
		dot -Tpng classes.dot -o doc/uml/classes.png
		dot -Tpng packages.dot -o doc/uml/packages.png
		rm -f classes.dot packages.dot



## Create HTML file
uml-html: check-virtual-env 
		@echo "<h1>Class diagram</h1>" > doc/uml/index.html
		@echo "<img source="classes.png">" >> doc/uml/index.html
		@echo "<h1>Package diagram</h1>" >> doc/uml/index.html
		@echo "<img source="packages.png">" >> doc/uml/index.html



## Generates UML diagrams and creates an .html file containing them
uml: uml-png uml-html
