
from django.urls import reverse_lazy
from .forms import AccommodationsForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Accommodations

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AccommodationListView(ListView):
    model = Accommodations

@method_decorator(login_required, name='dispatch')
class AccommodationCreateView(CreateView):
    model = Accommodations
    form_class = AccommodationsForm
    success_url = reverse_lazy('accommodations:accommodation-list')

@method_decorator(login_required, name='dispatch')
class AccommodationDetailView(DetailView):
    model = Accommodations
    context_object_name = 'accommodation' 

@method_decorator(login_required, name='dispatch')
class AccommodationDeleteView(DeleteView):
    model = Accommodations
    success_url = reverse_lazy("accommodations:accommodation-list")
    
    def get_object(self, queryset=None):
        id_accommodation = self.kwargs.get('id_accommodation')
        return self.model.objects.get(id_accommodation=id_accommodation)
    

@method_decorator(login_required, name='dispatch')
class AccommodationUpdateView(UpdateView):
    model = Accommodations
    form_class = AccommodationsForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('accommodations:accommodation-detail', args=[self.object.id_accommodation]) + '?ok'


#Vistas para el usuario
class AccommodationListViewUser(ListView):
    model = Accommodations
    template_name = "accommodation/accommodations_list_user.html"

class AccommodationDetailViewUser(DetailView):
    model = Accommodations
    template_name = "accommodation/accommodations_detail_user.html"
    context_object_name = 'accommodation' 

    def get_object(self, queryset=None):
        id_accommodation = self.kwargs.get('id_accommodation')
        return self.model.objects.get(id_accommodation=id_accommodation)