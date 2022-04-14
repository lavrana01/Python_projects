from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def user(request):
    return HttpResponse('hello world this is django')

