#REACT DJANGO

##DJANGO
Install Django:
$ pip3 install django djangorestframework

Create Project:
$ django-admin startproject project_name

Open Project on VScode:
cd project_name > code .

Create API folder:
$ django-admin startapp api

Settings Configuration:
1. project_name folder > settings.py
2. add this code in “INSTALLED_APPS”
3. 'api.apps.ApiConfig', 'rest_framework'

Settings View:
1. Open api folder > views.py > add code: 
“
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('Hello world')
”
2. Create new file "urls.py" on api folder
3. Open project_name folder > urls.py > add code:
“
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]
”
4. Open api folder > urls.py > add code:
"
from django.urls import path
from .views import main

urlpatterns = [
    path('', main)
]
"
Update Configuration:
1. $ python3 ./manage.py makemigrations (make ‘db.sqlite3’)
2. $ python3 ./manage.py migrate
3. $ python3 ./manage.py runserver
