#Listing 10_11: TicketSerializer
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket 
        fields = "__all__"
