from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from .models import Emprendimiento


class emprensListView(ListView):
    queryset = Emprendimiento.objects.all()
    template_name = "emprens/index.html"
#    def get_context_data(self, *args, **kwargs):
#        context = super(emprensListView, self).get_context_data(*args, **kwargs)
#        print(context)
#        return context

class emprensDetailView(DetailView):
    queryset = Emprendimiento.objects.all()
    template_name = "emprens/detail.html"
#    def get_context_data(self, *args, **kwargs):
#        context = super(emprensDetailView, self).get_context_data(*args, **kwargs)
#        print(context)
#        return context



