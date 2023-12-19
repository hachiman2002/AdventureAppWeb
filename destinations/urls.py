from django.urls import path
from .views import DestinationsListView, DestinationDetailView, DestinationDeleteView, DestinationCreateView, DestinationUpdateView, DestinationDetailViewUser, DestinationsListViewUser

destination_patterns = ([
    path('destinationsList/', DestinationsListView.as_view(), name='destination-list'),
    path('destinationDetail/<int:id_destination>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('destinationDelete/<int:id_destination>/', DestinationDeleteView.as_view(), name="destination-delete"),
    path('destinationCreate/', DestinationCreateView.as_view(), name="destination-create"),
    path('destinationUpdate/<int:id_destination>/', DestinationUpdateView.as_view(), name="destination-update"),
    path('destinationListUser/', DestinationsListViewUser.as_view(), name="destination-list-user"),
    path('destinationDetailUser/<int:id_destination>/', DestinationDetailViewUser.as_view(), name="destination-detail-user"),
],'destinations')