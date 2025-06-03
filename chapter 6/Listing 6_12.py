#Listing 6_12: is_authenticated
def myview(request):
	if request.user.is_authenticated:
		return HttpResponse("This message will be displayed only if a user is logged in")
	else:
		return redirect("login")
