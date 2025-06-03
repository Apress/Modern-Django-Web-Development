#Listing 4_4: rendering template
def index(request):
    template=loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))
