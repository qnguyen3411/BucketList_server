from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^tasks$', views.tasks),
    url(r'^tasks/(?P<id>\d+)/update$', views.update_tasks),
    url(r'^tasks/(?P<id>\d+)/delete$', views.delete_tasks),
]
