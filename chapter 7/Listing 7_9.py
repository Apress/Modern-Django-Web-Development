#Listing 7_9: GET, PUT and DELETE in serialized view
@api_view(['GET','PUT', 'DELETE'])
def ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    if request.method=='GET':        
        serialized_ticket = TicketSerializer(ticket)
        return Response(serialized_ticket.data)
