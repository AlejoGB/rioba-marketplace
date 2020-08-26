from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView , ListView , DetailView
from .models import Emprendimiento

class emprensBarrioView(ListView):
#    template_name = "emprens/index.html"
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
        return instance

#def emprensDetailView(request, pk=None, *args, **kwargs):
    #instance = Emprendimiento.objects.getById(pk)
    #if instance is None:
    #    raise Http404('no existe el emprendimiento') 
    # 
    #
    #instance = Emprendimiento.objects.get(pk=pk) #id
    #instance = get_object_or_404(Emprendimiento, pk=pk)    
##    #qs = Emprendimiento.objects.filter(id=pk)
##    #if qs.exists() and qs.count() == 1:
##    #    instance = qs.first()
##    #else:
##    #    raise Http404("no existe el emprendimiento")



    #try:
    #    instance = Emprendimiento.object.get(id=pk)
    #except Emprendimiento.DoesNotExist:
    #    print('no existe el emprendimiento')
    #except:
    #    print("huh?")
##    #context = {
##    #    'object': instance
##    #}
##    #return render(request, "emprens/detail.html", context)




