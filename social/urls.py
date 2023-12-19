from django.urls import path
from .views import SocialListView, SocialDetailView, SocialCreateView, SocialUpdateView, SocialDeleteView

social_patterns = ([
    path('socialList/', SocialListView.as_view(), name='social-list'),
    path('socialDetailView/<int:pk>/', SocialDetailView.as_view(), name="social-detail"),
    path('socialCreate', SocialCreateView.as_view(), name="social-create"),
    path('socialUpdate/<int:pk>/', SocialUpdateView.as_view(), name="social-update"),
    path('socialDelete<int:pk>/', SocialDeleteView.as_view(), name="social-delete"),
],'social')