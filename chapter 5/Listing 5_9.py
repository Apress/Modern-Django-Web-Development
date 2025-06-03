#Listing 5_9: Retrieve documents
def books(request, price):
    books = col.find({"price": {"$gt": price}})
    lst=[]
    for book in books:
        lst+="<h2>Title: {} \t Author: {} \t Price: {}</h2>".format(book['title'], book['author'], book['price'])
    return HttpResponse(lst)
