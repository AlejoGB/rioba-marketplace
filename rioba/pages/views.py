#from django.shortcuts import render
from django.views.generic import TemplateView 
from emprens.models import Emprendimiento


class index(TemplateView):
    template_name = 'pages/index.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['emprens'] = Emprendimiento.objects.all()
        #print(context)
        return context


class nosotros(TemplateView):
    template_name = 'pages/nosotros.html'


#def nosotros(request):
#    return render(request, 'pages/nosotros.html')