#from django.shortcuts import render
from django.views.generic import TemplateView



class index(TemplateView):
    template_name = 'pages/index.html'

class nosotros(TemplateView):
    template_name = 'pages/nosotros.html'

#def nosotros(request):
#    return render(request, 'pages/nosotros.html')