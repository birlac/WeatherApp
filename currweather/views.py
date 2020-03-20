from django.shortcuts import render
from django.http import HttpResponse

def hello(req):
    return HttpResponse('Weather Today..')

# Create your views here.
