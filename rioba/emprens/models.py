from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Emprendimiento(models.Model):
    # PUBLIC
    nombre = models.CharField(max_length=50)
    rubro  = models.CharField(max_length=50)       # definitivamente lista desplegable
    subrubro = models.CharField(max_length=50)     # lista desplegable?
    descripcion = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)   # validar?
    barrio = models.CharField(max_length= 70)      # Ciudad (lista desplegable?)
    ciudad = models.CharField(max_length = 50)     # Ciudad (lista desplegable?)
    cobertura = models.CharField(max_length=10)    # Distancia de cobertura de envios -> podria ser una lista de barrios o un medidor de distancia desde direccion
    contacto = models.CharField(max_length=100)    # Lista con mail, telefono, web, instagram, etc
    envio = models.CharField(max_length=100)       # envio a cargo del local? costo?
    horarios = models.CharField(max_length=100)    # disponibilidad para envios 
    # logo = IMAGEN

    
    # PRIVATE
    # value
    # opiniones
    owner = models.ForeignKey(CustomUser , on_delete=models.DO_NOTHING)


