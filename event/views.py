from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EventForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Events


@method_decorator(login_required, name='dispatch')
class EventListView(ListView):
    model = Events


@method_decorator(login_required, name='dispatch')
class EventCreateView(CreateView):
    model = Events
    form_class = EventForm
    success_url = reverse_lazy('events:event-list')

@method_decorator(login_required, name='dispatch')
class EventDetailView(DetailView):
    model = Events
    context_object_name = 'event' 

    def get_object(self, queryset=None):
        id_event = self.kwargs.get('id_event')
        return self.model.objects.get(id_event=id_event)
    

@method_decorator(login_required, name='dispatch')
class EventUpdateView(UpdateView):
    model = Events
    form_class = EventForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('events:event-detail', args=[self.object.id_event]) + '?ok'
    

@method_decorator(login_required, name='dispatch')
class EventDeleteView(DeleteView):
    model = Events
    success_url = reverse_lazy("events:event-list")
    
    def get_object(self, queryset=None):
        id_event = self.kwargs.get('id_event')
        return self.model.objects.get(id_event=id_event)
    

#Vistas para el usuario
class EventListViewUser(ListView):
    model = Events
    template_name = "event/events_list_user.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar el último destino al contexto
        context['ultimo_destino'] = Events.objects.latest('created')
        return context
    

class EventDetailViewUser(DetailView):
    model = Events
    template_name = "event/events_detail_user.html"
    context_object_name = 'event' 

    def get_object(self, queryset=None):
        id_event = self.kwargs.get('id_event')
        return self.model.objects.get(id_event=id_event)