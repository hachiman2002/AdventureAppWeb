"""
URL configuration for AdventureCuracautin_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.urls import core_patterns
from destinations.urls import destination_patterns
from event.urls import event_patterns
from eat.urls import eat_patterns
from accommodation.urls import accommodation_patterns
from social.urls import social_patterns
from pages.urls import pages_patterns

from django.conf import settings

urlpatterns = [
    #Path de core
    path('', include(core_patterns)),
    #path de destinations
    path('administration/', include(destination_patterns)),
    #path de events
    path('administration/', include(event_patterns)),
    #path de eat
    path('administration/', include(eat_patterns)),
    #path de accommodation
    path('administration/', include(accommodation_patterns)),
    #Path de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    #Path social
    path('administration/', include(social_patterns)),
    #Path de pages
    path('pages/', include(pages_patterns)),
    #Path de contact
    path('contact/', include('contact.urls')),
    #Path admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
