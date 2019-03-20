from django.shortcuts import render,redirect
from django.urls import resolve
from django.http import HttpRequest
from django.utils import timezone
from .models import User
from .forms import Signup

def index(request):

	return render(request,'home/web.html')


def _signup(request):
	if request.method == 'POST':

		form = Signup(request.POST)
		if form.is_valid():

			new_user = User(fullname=request.POST['fullname'],username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
			new_user.save()
	else:

		form = Signup()	

	context = { 'form':form }
	return render(request,'home/signup.html',context)

def _hello(request):
	return render(request,'home/hello.html')



