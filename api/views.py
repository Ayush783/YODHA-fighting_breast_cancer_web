from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def apihome(request):
    return HttpResponse("Welcome to YODHA fighting breast cancer api")

def signup(request):
    return HttpResponse("Welcome to YODHA fighting breast cancer sign up api")


