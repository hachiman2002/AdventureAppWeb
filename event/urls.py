from django.urls import path
from .views import EventListView, EventCreateView, EventDetailView, EventUpdateView,EventDeleteView,EventListViewUser,EventDetailViewUser

event_patterns = ([
    path('eventsList/', EventListView.as_view(), name='event-list'),
    path('eventCreate/', EventCreateView.as_view(), name="event-create"),
    path('eventDetail/<int:id_event>/', EventDetailView.as_view(), name='event-detail'),
    path('eventUpdate/<int:pk>/', EventUpdateView.as_view(), name="event-update"),
    path('eventDelete/<int:id_event>/', EventDeleteView.as_view(), name="event-delete"),
    path('eventListUser/', EventListViewUser.as_view(), name="event-list-user"),
    path('eventDetailUser/<int:id_event>/', EventDetailViewUser.as_view(), name="event-detail-user"),
],'events')
