#Listing 7_14: Registering router
from rest_framework.routers import DefaultRouter
from myapi.views import TicketViewSet

router = DefaultRouter()
router.register('tickets', TicketViewSet)
