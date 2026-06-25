from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request, "hello.html")

def fanju(request):
    return HttpResponse("hello world,here is fanju view")

def second(request):
    return HttpResponse("hello world,here is second view")
