#Listing 6_3: add_message() method 
from django.contrib import messages

messages.add_message(request, messages.SUCCESS, "Record updated successfully")
