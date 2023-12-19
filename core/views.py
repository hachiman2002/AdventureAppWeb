from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def us(request):
    return render(request, 'core/us.html')

def events(request):
    return render(request, 'core/events.html')

def eat(request):
    return render(request, 'core/eat.html')

def accommodation(request):
    return render(request, 'core/accommodation.html')

