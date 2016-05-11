#!/bin/bash

vagrant up
vagrant ssh --command '
python3 manage.py runserver 127.0.0.1:8080 
'
