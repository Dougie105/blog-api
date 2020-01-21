## In your terminal input the following...
```python
django-admin startproject dog_project .

python manage.py startapp poodle

pipenv shell

python manage.py migrate

python manage.py runserver

```
## Go to Models
```python
# In models.py

from django.contrib.auth.models import User
from django.db import models

class Poodle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```
## Go to admin.py
```python

from django.contrib import admin
from .models import Poodle

admin.site.register(Poodle) #name of your model/models

```
## Go to settings and under INSTALLED APPS, ADD...
```python
'poodle.apps.PoodleConfig,'
```

## Go back to terminal and type...
```python

./manage.py makemigrations

./manage.py migrate

#should be able to check in admin, but first you need to create a superuser

./manage.py createsuperuser

# un terrelldouglas
# pw 12

./manage.py runserver #if you didnt already close it out.
```
## You can now look in admin and should be able to add a new post.

## Otherwise do to your project level urls.py

```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('poodle.urls')),
]
```

## Add a urls.py to your app level folder now. In ut you are going to type:

```python

from django.urls import path
from .views import PoodleList

urlpatterns = [
    path('poodles/', PoodleList.as_view(), name='poodle_list'),
]

```

## But you need to create a PoodleList somewhere, so go to views.py.

```python

from .models import Poodle
from .serializers import PoodleSerializer
from rest_framework import generics

class PoodleList(generics.ListCreateAPIView):
    #templates/models
    queryset = Poodle.objects.all()

    serializer_class = PoodleSerializer

```

## Now install djangorestframework

## update the settings again

```python
# Add another section to INSTALLED_APPS

'rest_framework',

# Then at the bottom of settings you want to do the following, for now.

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.AllowAny'
    ]
}
```

## Create a serializers.py in your app

```python

from rest_framework import serializers

from .models import Poodle

class PoodleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poodle
        fields = [
            'id', 'author', 'title', 'created_at'
        ]

```
## SHOULD NOW BE ABLE TO GET A PAGE ON http://127.0.0.1:8000/api/v1/poodles/

## Go back into the app urls.py and add another pattern

```python
# It should now look like the following

from django.urls import path
from .views import PoodleList, PoodleDetail

urlpatterns = [
    path('poodles/', PoodleList.as_view(), name='poodle_list'),

    path('poodles/<int:pk>', PoodleDetail.as_view(), name='poodle_detail'),
]

```
# Now go to views, It should now look like

```python

from .models import Poodle
from .serializers import PoodleSerializer
from rest_framework import generics

class PoodleList(generics.ListCreateAPIView):
    #templates/models
    queryset = Poodle.objects.all()
    serializer_class = PoodleSerializer

class PoodleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poodle.objects.all()
    serializer_class = PoodleSerializer

```

## You chould now have full CRUD

# Docker Time

### Touch Dockerfile

```
FROM python:3.7-slim

# Environmental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

COPY Pipfile /code
COPY Pipfile.lock /code/

# Install dependencies
RUN pip install pipenv && pipenv install --system

COPY . /code
```
## Then
```docker build .```

## Then
```touch docker-compose.yml```

## In Terminal
```nano```

## In nano
```
version '3.7'

services:
    web:
        build:
        command: python /code/manage.py runserver 0.0.0.0.8000
```

## save changes
```docker-compose up --build```