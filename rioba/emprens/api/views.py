from rest_framework import generics
from emprens.models import Emprendimiento , Producto
from .serializers import EmprendimientoSerializer


class EmprendimientoListView(generics.ListAPIView):
    lookup_field        = 'slug'
    serializer_class    = EmprendimientoSerializer

    def get_queryset(self):
        return Emprendimiento.objects.all()

    


class EmprendimientoCRUDView(generics.RetrieveAPIView): # por ahora solo RETRIEVE    # Detailview , CreateView , FormView
                                                        # una vez implementados los usuarios: CREATE UPDATE DELETE
    serializer_class    = EmprendimientoSerializer
    lookup_field        = 'slug'
    


    def get_queryset(self):
        return Emprendimiento.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Emprendimiento.objects.get(pk=pk)

    # def get_byBarrio(self):
    #     barrio = self.kwargs.get('barrio')
    #     return Emprendimiento.objects.get(barrio=barrio)
    
    