"""Defines URL patterns for users."""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'

urlpatterns = [
    # User login page (class-based view)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 

    # User registration page (use simple view that accepts GET and POST)
    path('register/', views.register, name='register'),

    # User logout page (use simple view that accepts GET and POST)
    path('logout/', views.logout_view, name='logout'), ]