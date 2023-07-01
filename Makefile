.PHONY: build install test coverage qr_weefee

build:
	python3 -m build

install:
	pip3 install .

test:
	coverage run --source=weefee -m unittest discover
	coverage report -m

qr_weefee:
	qr_weefee