# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^decorator_index/$', views.index_decorator, name='logged_index'),
    url(r'^aspect_index/$', views.index_aspect, name='logged_aspect'),
]