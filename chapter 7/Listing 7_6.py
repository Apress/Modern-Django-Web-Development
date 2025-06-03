#Listing 7_6: ModelSerializer
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket 
        fields = "__all__"
