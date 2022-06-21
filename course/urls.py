## @brief urls for the course app.

from importlib.resources import path
from django.urls import include, re_path
from django.contrib import admin
from . import views

## @brief url patterns for the course app.
urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^(?P<course_id>[0-9]+)/detail/$', views.detail, name='detail'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^(?P<assignment_id>[0-9]+)/upload_submission/$', views.upload_submission, name='upload_submission'),
    re_path(r'^(?P<course_id>[0-9]+)/view_assignments/$', views.view_assignments, name='view_assignments'),
    re_path(r'^(?P<course_id>[0-9]+)/view_resources/$', views.view_resources, name='view_resources'),
]
