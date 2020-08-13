from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class registro(generic.CreateView):
    form_class = CustomUserCreationForm
    succes_url = reverse_lazy('login')
    template_name = 'registration/registro.html'


