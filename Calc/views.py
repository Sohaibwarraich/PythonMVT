from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'home.html',{'name':'ali'})

def add(request):
	nu1 = int(request.POST['num1'])
	nu2 = int(request.POST['num2'])
	res = nu1+nu2
	return render(request, 'result.html',{'result':res})

def myview(request):
	return HttpResponse('My view ...')