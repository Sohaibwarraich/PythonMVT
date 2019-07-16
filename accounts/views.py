from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def registration(request):
	if request.method =='POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username already taken')
				return redirect('registration')
			if User.objects.filter(email =email).exists():
				messages.info(request,'Email already taken')
				return redirect('registration')

			else:
				user = User.objects.create_user(username = username, password = password1,email =email,first_name=first_name,last_name=last_name)
				user.save()
		else:
			print('Password Missmatch')
			return redirect('registration')

		return redirect('/')
	else:
		return render(request, 'registration.html')
