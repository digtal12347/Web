from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello world")

def live1(request):
    return HttpResponse("hello world,here is live1 view")

def live2(request):
    return HttpResponse("hello world,here is live2 view")
