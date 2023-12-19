from django.urls import path
from .views import EatsListView,EatCreateView,EatDetailView,EatUpdateView,EatDeleteView,EatListViewUser,EatDetailViewUser

eat_patterns = ([
    path('eatsList/', EatsListView.as_view(), name='eat-list'),
    path('eatCreate/', EatCreateView.as_view(), name="eat-create"),
    path('eatDetail/<int:pk>/', EatDetailView.as_view(), name='eat-detail'),
    path('eatUpdate/<int:pk>/', EatUpdateView.as_view(), name="eat-update"),
    path('eatDelete/<int:id_eat>/', EatDeleteView.as_view(), name="eat-delete"),
    path('eatListUser/', EatListViewUser.as_view(), name="eat-list-user"),
    path('eatDetailUser/<int:id_eat>/', EatDetailViewUser.as_view(), name="eat-detail-user"),

],'eats')