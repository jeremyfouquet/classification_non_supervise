.ONESHELL:
.DEFAULT_GOAL:= run
P3 = python3
PYTHON= ./venv/bin/python3
PIP= ./venv/bin/pip

venv/bin/activate: requirements.txt
	$(P3) -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

venv: venv/bin/activate
	. ./venv/bin/activate

run: venv
	$(PYTHON) main.py

clean:
	rm -rf __pycache__
	rm -rf venv

.PHONY: run clean