#Listing 4_21 : addbook view to save the ModelForm
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Book added successfully</h2>")
