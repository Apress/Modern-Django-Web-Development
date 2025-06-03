#Listing 5_11: Retrieve single document
def getbook(request, id):
    book = col.find_one({"id":id})
    return HttpResponse("<h2>Title: {} \t Author: {} \t Price: {}</h2>".format(book['title'], book['author'], book['price']))
