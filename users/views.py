# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import aspectlib
from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world. You're at index.")

@login_required(login_url='/login')
def index_decorator(request):
    return HttpResponse("Hello, world. You're at the decorator index, if you're logged in.")

@aspectlib.Aspect
def strip_return_value(request):
    if not request.user.is_authenticated:
        print('No autenticado')
    
    yield aspectlib.Proceed(
        request, 
        args={"message": "Hello, world. You're at the aspects index, if you're logged in."}
    )

@strip_return_value
def index_aspect(request, **kwargs):
    return HttpResponse(kwargs['args']['message'])
