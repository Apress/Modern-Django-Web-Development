#Listing 7_4: Ticket model
from django.db import models

class Ticket(models.Model):
    flight_number = models.CharField(max_length=10)
    passenger_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    seat_number = models.CharField(max_length=5)
