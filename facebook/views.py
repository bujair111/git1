from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render (request, 'facebook_templates/facebook.html')

def signup(request):
    return render (request, 'facebook_templates/signup.html')

def mypage(request):
    return render (request, 'facebook_templates/mypage.html')        