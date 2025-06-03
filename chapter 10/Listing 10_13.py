#Listing 10_13: URL routes
urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('tickets/', views.TicketListCreateView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketRetrieveUpdateDeleteView.as_view(), name='ticket-detail'),
]
