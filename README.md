# cd-docker-ansible

pip install django==1.9
pip install virtualenv

django-admin startproject todobackend

virtualenv venv


in each VM
source venv/bin/activate
pip install django==1.9
pip install djangorestframework==3.3
pip install django-cors-headers==1.1
python manage.py startapp todo
pip install mysql-python
pip install pinnochio
pip install coverage

make model
python manage.py makemigrations todo


to run server
python manage.py runserver