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


