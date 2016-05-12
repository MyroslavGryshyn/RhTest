#!/bin/bash

workon rh-test
pip install -r /vagrant/requirements.txt

python /vagrant/manage.py makemigrations
python /vagrant/manage.py migrate
