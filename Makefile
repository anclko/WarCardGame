# ---------------------------------------------------------
# Setup a venv and install packages.
#

run:
	python main.py

# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-src:
	$(call FOREACH,clean)

clean-all: clean clean-doc clean-src
	rm -rf .venv


# ---------------------------------------------------------
# Test all the code at once.
#
coverage:
	$(
pylint:
	$(call FOREACH,pylint)

flake8:
	$(call FOREACH,flake8)

lint: flake8 pylint

test:
	$(call FOREACH,test)


///////////////////////////////////////////


## Checks if virtual environment exists, if not then creates it
venv:
		test -d $(VENV) || python3 -m venv $(VENV)
## Now you should enter . .venv/Scripts/activate in terminal if you are on Windows
## or . .venv/bin/activate if you are on Mac/Linux
## Note that this will vary between terminals



## Displays which version the python interpreter is on
version: check-virtual-env
		@printf "Python executable version: "
		@$(PYTHON) --version



check-virtual-env:
		@echo virtual-env: $${VIRTUAL_ENV?"Please source your .venv/"}



## Installs pip packages based on package list in REQUIREMENTS.txt
install: check-virtual-env
		pip install -q -r REQUIREMENTS.txt
		$(PYTHON) -m pip install --upgrade -q pip



## Shows installed pip packages
installed: check-virtual-env
		$(PYTHON) -m pip list



## Check pylint coverage
pylint: check-virtual-env
		@for py in src/*.py; do echo "Linting $$py"; pylint -d C0103 -rn $$py; done
		@for py in src/*/*.py; do echo "Linting $$py"; pylint -d C0103 -rn $$py; done
		@for py in src/*/*/*.py; do echo "Linting $$py"; pylint -d C0103 -rn $$py; done



## Check flake8 coverage
flake8: check-virtual-env
		@$(call MESSAGE,$@)
		-flake8 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg,$(VENV),venv,*.pyc

## Check pylint and flake8 coverage
lint: check-virtual-env 
		$(MAKE) pylint
		$(MAKE) flake8



## Clear temporary interpeter cache and virtual environment files
clean:
		rm -rf src/__pycache__
		rm -rf src/*/__pycache__
		rm -rf src/*/*/__pycache__
		rm -rf src/*/*/*/__pycache__
		rm -rf src/*.pyc
		rm -rf src/*/*.pyc
		rm -rf src/*/*/*.pyc
		rm -rf src/*/*/*/*.pyc
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
		pdoc -o doc/api ./src/*.py ./src/*/*.py ./src/*/*/*.py



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



## Generate UML diagrams from code
uml-png: check-virtual-env
		@$(call message, $@)
		install -d doc/uml
		pyreverse ./src/*.py ./src/include/*.py
		pyreverse ./src/include/player/*.py ./src/include/utils/*.py ./src/tests/*.py
		dot -Tpng classes.dot -o doc/uml/classes.png
		dot -Tpng packages.dot -o doc/uml/packages.png
		rm -f classes.dot packages.dot



## Create an index HTML file with both images
uml-html: check-virtual-env 
		@echo "<h1>Class diagram</h1>" > doc/uml/index.html
		@echo "<img src="classes.png">" >> doc/uml/index.html
		@echo "<h1>Package diagram</h1>" >> doc/uml/index.html
		@echo "<img src="packages.png">" >> doc/uml/index.html




## Generates UML diagrams and creates an .html file containing them
uml: uml-png uml-html
