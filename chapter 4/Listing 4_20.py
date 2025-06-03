#Listing 4_20: ModelForm class

from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
