#Listing 7_7: Using serializer in DRF view
from .models import Ticket
from .serializers import TicketSerializer

@api_view() 
def tickets(request): 
    tickets = Ticket.objects.all()
    serialized_tickets = TicketSerializer(tickets, many=True)
    return Response(serialized_tickets.data)
