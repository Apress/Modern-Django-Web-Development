#Listing 4_26: MyView class
class MyView(View):
    def get(self, request):
        return render(request, "mytemplate.html", {})    
    def post(self, request):
        name=request.POST['name']
        return HttpResponse(name)
