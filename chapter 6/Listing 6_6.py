#Listing 6_6: index view
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        password = request.POST.get("password")
        if name =="" or password =="":
            messages.error(request, "required")            
        if len(request.POST.get('password'))<9:
            messages.warning(request, "Weak Password")
        if name in ['admin', 'manager', 'superuser']:
            messages.error(request, "Username Not Available")
        else:
            messages.success(request, "Login Successful. Welcome "+name)
            return HttpResponse("success")
    
    return render(request, "index.html", {})
