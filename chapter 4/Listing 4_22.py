#Listing 4_22: getbook view showing pre-populated ModelForm
from .forms import BookForm

def getbook(request, author):
    b1 = Book.objects.get(author=author)
    form = BookForm(instance=b1)
    context={'form' : form}
    return render(request, "bookform.html", context)
