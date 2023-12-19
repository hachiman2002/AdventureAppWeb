from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Pages
from .forms import PageForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
# Create your views here.
@method_decorator(login_required, name='dispatch')
class PageListView(ListView):
    model = Pages

@method_decorator(login_required, name='dispatch')
class PagesDetailView(DetailView):
    model = Pages
    context_object_name = 'pages'
    
@method_decorator(login_required, name='dispatch')
class PageCreateView(CreateView):
    model = Pages
    form_class = PageForm
    success_url = reverse_lazy('pages:page-list')

@method_decorator(login_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Pages
    success_url = reverse_lazy("pages:page-list")
    
@method_decorator(login_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Pages
    form_class = PageForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('pages:page-detail', args=[self.object.id]) + '?ok'
    
class PagesDetailViewUser(DetailView):
    model = Pages
    template_name = 'pages/pages_detail_user.html'
    context_object_name = 'pages'