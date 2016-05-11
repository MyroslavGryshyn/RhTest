#!/bin/bash

pip3 install -r /vagrant/requirements.txt
python3 manage.py makemigrations
python3 /vagrant/manage.py migrate
