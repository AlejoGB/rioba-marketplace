from django.db import models
from accounts.models import CustomUser
import random
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image_path(instance , filename):
    new_filename = random.randint(1,154125125)
    name , ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f"emprens/{new_filename}/{final_filename}"



# Create your models here.

class Emprendimiento(models.Model):
    # PUBLIC
    nombre = models.CharField(max_length=50)
    rubro  = models.CharField(max_length=50)       # definitivamente lista desplegable
    subrubro = models.CharField(max_length=50)     # lista desplegable?
    descripcion = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=upload_image_path , null=True , blank=True)
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

    def __str__(self):
        return self.nombre #, self.rubro , self.subrubro , self.barrio , self.ciudad


