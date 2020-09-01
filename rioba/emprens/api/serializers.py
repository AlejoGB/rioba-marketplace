from rest_framework import serializers
from emprens.models import Emprendimiento , Producto


class EmprendimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields = [
            'pk',
            'nombre',
            'descripcion',
            'rubro',
            'logo',

            'cont_mail',
            'cont_insta',
            'cont_whatsapp',
            
            'barrio',
            'cobertura',
            'horarios',
            'envio',
        ]
        read_only_fields = ['pk']

        # convierte a JSOn
        # valida data
    