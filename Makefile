
venv:
	python3 -m virtualenv venv

install:
	./venv/bin/pip3 install -r requirements.txt

build:
	./venv/bin/python3 src/uplink.py --path=$(path)
