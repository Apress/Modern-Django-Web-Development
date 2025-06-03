#Listing 7_11: TicketListView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer

class TicketListView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serialized_tickets = TicketSerializer(tickets, many=True)
        return Response(serialized_tickets.data)
    def post(self, request):
        serialized_ticket = TicketSerializer(data=request.data)
        serialized_ticket.is_valid(raise_exception=True)
        serialized_ticket.save()
        return Response(serialized_ticket.validated_data,status.HTTP_201_CREATED)
