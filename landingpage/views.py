from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
	return render(request, 'landingpagedesign/index.html')


def register(request):
	return render(request, 'landingpagedesign/register.html')


def login(request):
	return render(request, 'landingpagedesign/login.html')	