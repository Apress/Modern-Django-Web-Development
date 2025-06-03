#Listing 3_4 : update Url patterns
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("books/", views.books, name="books"),
]
