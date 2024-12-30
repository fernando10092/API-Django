from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    ###################### INSERI ##########################
    path('', views.get_users, name='get_all_users'),
    path('data/', views.user_manager)
]
