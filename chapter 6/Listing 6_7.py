#Listing 6_7: login view
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Login successful. Hello {}".format(user))	
			return redirect('index')
		else:
			messages.error(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	
	else:
		return render(request, 'login.html', {})
