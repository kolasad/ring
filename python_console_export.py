import this
from notifications.models import Flower
from django.contrib.auth.models import User
import requests
Flower.objects.create(color=1, name='iris', description='nice one')
flower.id
flower.pk
flower.color
flower = Flower.objects.all().first()
flower.type
user=User.objects.first()
flower.name = 'daisy'
flower.name
flower.user = user
flower.user
flower.user_id
flower.user.id
flower.owner = user
flower.save()
import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='iris', description='nice one', user=)

import random
random.randint(1,3)
user = User.objects.create(username='John', email='user@user.com')
import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='iris', description='nice one', user_id=random.randint(1,2))

import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='iris', description='nice one', user__id=random.randint(1,2))

import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='iris', description='nice one', user=random.randint(1,2))

import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='iris', description='nice one', owner=random.randint(1,2))

import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='iris', description='nice one', owner_id=random.randint(1,2))

import random
for x in range(100):
    Flower.objects.create(color=random.randint(1,3), name='daisy', description='nice one', owner_id=random.randint(1,2))

Flower.objects.filter(owner_id=1).count()
from notifications.models import Flower
Flower.objects.all().values('owner_id')
from django.db.models import Count
Flower.objects.all().values('owner_id').annotate(flowers_count=Count('owner_id'))
{'key': 123, 'message': 'Hello there!'}
req_data = {'key': 123, 'message': 'Hello there!'}
req_data.get('message')
req_data.get('msf2')
a=req_data.get('msf2')
type(a)
print(a)
a=req_data.get('msf2', 'Some str')
a
req_data['msf2']
req_data['message']
response = requests.get('google.com')
response = requests.get('https://google.com')
response = requests.post('http://127.0.0.1:8000/mails/send')
response.text
from notifications.models import Mail
Mail.objects.create()
from django.contrib.auth.models import User
user = User.objects.first()
user
user.set_password('admin123')
user.save()
cleaned_data = {'login': 'admin', 'email': 'admin@asd.com', 'password': 'admin'}
cleaned_data['login']
cleaned_data['message']
cleaned_data.get('message')
cleaned_data.get('message', 'DEFAULT')
import requests
response = requests.post('http://127.0.0.1:8000/mails/send', json={'message': 'Hello', 'recipient': 'kolasadom@gmail.com'})
response = requests.post('http://127.0.0.1:8000/mails/send', json={'message': 'Hello', 'recipient': 'kolasadom@gmail.com'}, auth=('admin', 'admin123'))
response = requests.post('http://127.0.0.1:8000/mails/send', json={'message': 'Hello', 'recipient': 'kolasadom@gmail.com', 'subject': "Nice email'"}, auth=('admin', 'admin123'))