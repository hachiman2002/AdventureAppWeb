from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EatsForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Eats


# Create your views here.
@method_decorator(login_required, name='dispatch')
class EatsListView(ListView):
    model = Eats

@method_decorator(login_required, name='dispatch')
class EatCreateView(CreateView):
    model = Eats
    form_class = EatsForm
    success_url = reverse_lazy('eats:eat-list')


@method_decorator(login_required, name='dispatch')
class EatDetailView(DetailView):
    model = Eats
    context_object_name = 'eat' 


@method_decorator(login_required, name='dispatch')
class EatUpdateView(UpdateView):
    model = Eats
    form_class = EatsForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('eats:eat-detail', args=[self.object.id_eat]) + '?ok'

@method_decorator(login_required, name='dispatch')
class EatDeleteView(DeleteView):
    model = Eats
    success_url = reverse_lazy("eats:eat-list")
    
    def get_object(self, queryset=None):
        id_eat = self.kwargs.get('id_eat')
        return self.model.objects.get(id_eat=id_eat)
    


#Vistas para el usuario
class EatListViewUser(ListView):
    model = Eats
    template_name = "eat/eats_list_user.html"


class EatDetailViewUser(DetailView):
    model = Eats
    template_name = "eat/eats_detail_user.html"
    context_object_name = 'eat' 

    def get_object(self, queryset=None):
        id_eat = self.kwargs.get('id_eat')
        return self.model.objects.get(id_eat=id_eat)

