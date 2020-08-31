from django import forms
from emprens.models import Emprendimiento , Producto

class EmprendimientoForm(forms.ModelForm):
    class Meta:
        model = Emprendimiento
        fields = ('nombre' , 'rubro' , 'subrubro' , 'descripcion' , 'logo' , 'direccion' , 'barrio' , 'ciudad' , 'cobertura' , 'contacto' , 'envio' , 'horarios' )

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre' , 'categoria' , 'descripcion' , 'imagen' , 'precio' )    