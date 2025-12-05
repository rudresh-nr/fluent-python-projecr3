'''Defines URL patterns for learning_logs.'''

from django.urls import path as url
from . import views

urlpatterns = [
    # Home page
    url('', views.index, name='index'),
]