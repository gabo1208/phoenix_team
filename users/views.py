# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world. You're at index.")

@login_required(login_url='/admin/')
def index_decorator(request):
    return HttpResponse("Hello, world. You're at the index, if you're logged in.")
