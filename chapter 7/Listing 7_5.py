#Listing 7_5: serializers.py
from rest_framework import serializers

class TicketSerializer(serializers.Serializer):
    flight_number = serializers.CharField(max_length=10)
    passenger_name = serializers.CharField(max_length=100)
    departure_time = serializers.DateTimeField()
    seat_number = serializers.CharField(max_length=5)
