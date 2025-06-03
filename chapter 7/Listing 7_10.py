#Listing 7_10: HyperlinkedModelSerializer class
from rest_framework import serializers
from .models import Ticket
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url', 'flight_number', 'passenger_name', 'departure_time', 'seat_number']
        extra_kwargs = {
            'url': {'view_name': 'ticket-detail', 'lookup_field': 'pk'}  
        }
