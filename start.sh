#!/bin/bash

echo "Installing plugin to avoid issue vith mon=unting shared folders"
vagrant plugin install vagrant-vbguest

vagrant up
vagrant ssh --command '
workon rh-test
python /vagrant/manage.py runserver 127.0.0.1:8080
'
