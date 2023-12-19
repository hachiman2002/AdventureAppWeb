from django.urls import path
from core import views

core_patterns = [
    path('', views.index, name="index"),
    path('us/', views.us, name="us"),
    path('eat/', views.eat, name="eat"),
    path('accommodation/', views.accommodation, name="accommodation"),
]
