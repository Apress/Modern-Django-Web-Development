#Listing 4_16: forms.py
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(label="Title ", max_length=50)
    author = forms.CharField(label='Author ', max_length=50)
    price = forms.IntegerField(label='Price ')
    publisher = forms.CharField(label = 'Publisher ', max_length=50)
    ebook = forms.BooleanField(initial=True)
