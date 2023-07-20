from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def grapes(request):
    return HttpResponse("this is my fruits app1")
