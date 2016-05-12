# RhTest
**Requirements:**
  
1) Vagrant

2) VirtualBox
  
  
  **Instructions to run this app**

1) Clone this project

2) Run 'bash start.sh'

3) Open frontend on host machine: http://127.0.0.1:9999

  **To run tests from host machine:**
  
1) vagrant ssh --command '
source /home/vagrant/.virtualenvs/rh-test/bin/activate
cd /vagrant
quote> python manage.py test'

