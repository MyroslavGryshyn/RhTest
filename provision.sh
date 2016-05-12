#!/bin/bash

source /home/vagrant/.virtualenvs/rh-test/bin/activate
pip install -r /vagrant/requirements.txt

python /vagrant/manage.py makemigrations
python /vagrant/manage.py migrate
