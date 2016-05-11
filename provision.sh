#!/bin/bash

workon rh-test
pip install -r /vagrant/requirements.txt

python3 /vagrant/manage.py makemigrations
python3 /vagrant/manage.py migrate
