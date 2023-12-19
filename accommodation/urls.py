from django.urls import path
from .views import AccommodationListView,AccommodationCreateView,AccommodationDetailView,AccommodationDeleteView,AccommodationUpdateView,AccommodationListViewUser,AccommodationDetailViewUser

accommodation_patterns = ([
    path('accommodationList/', AccommodationListView.as_view(), name='accommodation-list'),
    path('accommodationCreate/', AccommodationCreateView.as_view(), name="accommodation-create"),
    path('accommodationDetail/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
    path('accommodationDelete/<int:id_accommodation>/', AccommodationDeleteView.as_view(), name="accommodation-delete"),
    path('accommodationUpdate/<int:pk>/', AccommodationUpdateView.as_view(), name="accommodation-update"),
    path('accommodationListUser/', AccommodationListViewUser.as_view(), name="accommodation-list-user"),
    path('accommodationDetailUser/<int:id_accommodation>/', AccommodationDetailViewUser.as_view(), name="accommodation-detail-user"),
], 'accommodations')