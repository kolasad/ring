from django.urls import path

from authorization.views import register_view

urlpatterns = [
    path('register', register_view, name='register')
]
