from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView , ListView , DetailView
from .models import Emprendimiento

#@login_required(login_url='/empren/sign-in/')

class emprensBarrioView(ListView):
    template_name = "emprens/rioba.html"
    def get_queryset(self,*args,kwargs):
        request = self.request
    #    return Emprendimiento.objects.getByBarrio(request)
        return Emprendimiento.objects.all().getByBarrio(request)

class emprensListView(ListView):
    #queryset = Emprendimiento.objects.all()
    template_name = "emprens/index.html"
#    def get_context_data(self, *args, **kwargs):
#        context = super(emprensListView, self).get_context_data(*args, **kwargs)
#        print(context)
#        return context
    def get_queryset(self,*args,**kwargs ):
        request = self.request
        return Emprendimiento.objects.all()

class emprensDetailView(DetailView):
#    queryset = Emprendimiento.objects.all()
    template_name = "emprens/detail.html"
#    def get_context_data(self, *args, **kwargs):
#        context = super(emprensDetailView, self).get_context_data(*args, **kwargs)
#        print(context)
#        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Emprendimiento.objects.getById(pk)   
        if instance is None:
            raise Http404('no existe el emprendimiento')
        return instance
    # def get_queryset(self,*args,**kwargs ):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Emprendimiento.objects.filter(pk=pk)
    #    instance = Emprendimiento.objects.filter(pk=pk)
    #    if instance is None:
    #         raise Http404('no existe el emprendimiento')
    #    return instance

class emprensSlugView(DetailView):
    queryset = Emprendimiento.objects.all()
    template_name = "emprens/detail.html"        
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Emprendimiento.objects.get(slug=slug , active=True)
        except Emprendimiento.DoesNotExist:
            raise Http404("emprendimiento no encontrado..")
        except Emprendimiento.MultipleObjectsReturned:
            qs = Emprendimiento.objects.filter(slug=slug , active=True)
            instace = qs.first()
        except:
            raise Http404(" nope ")
        print(instance.id)
#        try:
#            subinstance = Producto.objects.get( emprendimiento=instance.id )
#        return instance






