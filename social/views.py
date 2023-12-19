from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Social
from .forms import SocialForm
# Create your views here.
@method_decorator(login_required, name='dispatch')
class SocialListView(ListView):
    model = Social

@method_decorator(login_required, name='dispatch')
class SocialDetailView(DetailView):
    model = Social
    context_object_name = 'social'
    
@method_decorator(login_required, name='dispatch')
class SocialCreateView(CreateView):
    model = Social
    form_class = SocialForm 
    success_url = reverse_lazy('social:social-list')

@method_decorator(login_required, name='dispatch')
class SocialDeleteView(DeleteView):
    model = Social
    success_url = reverse_lazy("social:social-list")
    
@method_decorator(login_required, name='dispatch')
class SocialUpdateView(UpdateView):
    model = Social
    form_class = SocialForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('social:social-detail', args=[self.object.id]) + '?ok'

