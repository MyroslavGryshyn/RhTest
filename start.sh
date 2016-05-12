#!/bin/bash

echo "Installing plugin to avoid issue vith mon=unting shared folders"
vagrant plugin install vagrant-vbguest

vagrant up
vagrant ssh --command '
source /home/vagrant/.virtualenvs/rh-test/bin/activate
python /vagrant/manage.py runserver 0.0.0.0:8080
'
