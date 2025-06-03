#Listing 7_8: GET and POST with serialized view
from rest_framework import status
@api_view(['GET', 'POST']) 
def tickets(request): 
    if request.method=='GET':
        tickets = Ticket.objects.all()
        serialized_tickets = TicketSerializer(tickets, many=True)
        return Response(serialized_tickets.data)
    
    elif request.method=='POST':
                serialized_ticket = TicketSerializer(data=request.data)
                serialized_ticket.is_valid(raise_exception=True)
                serialized_ticket.save()
                return Response(serialized_ticket.validated_data,status  .HTTP_201_CREATED)
