#Listing 6_8: logout view
def logout_user(request):
	logout(request)
	messages.info(request, ( "You Were Logged Out!"))
	return redirect('index')
