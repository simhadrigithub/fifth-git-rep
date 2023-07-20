from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def nature(request):
    return HttpResponse("this is my first farmers app ")

