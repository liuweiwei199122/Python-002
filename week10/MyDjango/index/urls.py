from django.contrib import admin
from django.urls import path, include, re_path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.login),
	path('login2', views.login2)
]