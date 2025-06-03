#Listing 6_11: login_required decorator 

from django.contrib.auth.decorators import login_required

@login_required(login_url="../login/" )
def myview(request):
	return HttpResponse("This message will be displayed only if a user is logged in")
