from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import DestinationsForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Destinations

# Create your views here.
@method_decorator(login_required, name='dispatch')
class DestinationsListView(ListView):
    model = Destinations

@method_decorator(login_required, name='dispatch')
class DestinationDetailView(DetailView):
    model = Destinations
    context_object_name = 'destination' 

    def get_object(self, queryset=None):
        id_destination = self.kwargs.get('id_destination')
        return self.model.objects.get(id_destination=id_destination)

@method_decorator(login_required, name='dispatch')
class DestinationCreateView(CreateView):
    model = Destinations
    form_class = DestinationsForm
    success_url = reverse_lazy('destinations:destination-list')

@method_decorator(login_required, name='dispatch')
class DestinationDeleteView(DeleteView):
    model = Destinations
    success_url = reverse_lazy("destinations:destination-list")
    
    def get_object(self, queryset=None):
        id_destination = self.kwargs.get('id_destination')
        return self.model.objects.get(id_destination=id_destination)

@method_decorator(login_required, name='dispatch')
class DestinationUpdateView(UpdateView):
    model = Destinations
    form_class = DestinationsForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('destinations:destination-detail', args=[self.object.id_destination]) + '?ok'
    
        
    def get_object(self, queryset=None):
        id_destination = self.kwargs.get('id_destination')
        return self.model.objects.get(id_destination=id_destination)
    
#Vistas para el usuario
class DestinationsListViewUser(ListView):
    model = Destinations
    template_name = "destinations/destinations_list_user.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el último destino al contexto
        context['ultimo_destino'] = Destinations.objects.latest('created')
        return context
    
class DestinationDetailViewUser(DetailView):
    model = Destinations
    template_name = "destinations/destinations_detail_user.html"
    context_object_name = 'destination' 

    def get_object(self, queryset=None):
        id_destination = self.kwargs.get('id_destination')
        return self.model.objects.get(id_destination=id_destination)