from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import pre_save , post_save
from .utils import unique_slug_generator
import random
import os
from django.urls import reverse

def get_filename_ext(filepath): #genera la extension del archivo para el path
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image_path(instance , filename): #genera un path para la imagen con un numero aleatorio
    new_filename = random.randint(1,154125125)
    name , ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f"emprens/{new_filename}/{final_filename}"


class EmprendimientoQuerySet(models.query.QuerySet):
    def barrio(self):
            return self.filter(barrio__iexact=barrio)
    def active(self):
            return self.filter(active=True)


class EmprendimientoManager(models.Manager):
    def get_queryset(self):
        return EmprendimientoQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()

    def getById(self, id):
        qs = self.get_queryset().filter(id=id)#Emprendimiento.objects.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None
    def getByBarrio(self):#Emprendimiento.objects.getbyBarrio()
        return self.get_queryset.barrio().active()
    
# Create your models here.

class Emprendimiento(models.Model):
    # PUBLIC
    nombre                  = models.CharField(max_length=50)
    slug                    = models.SlugField(blank=True , unique=True)
    rubro                   = models.CharField(max_length=50)       # definitivamente lista desplegable
    subrubro                = models.CharField(max_length=50)     # lista desplegable?
    descripcion             = models.CharField(max_length=200)
    logo                    = models.ImageField(upload_to=upload_image_path , null=True , blank=True)
    direccion               = models.CharField(max_length=200)   # validar?
    barrio                  = models.CharField(max_length= 70)      # Ciudad (lista desplegable?)
    ciudad                  = models.CharField(max_length = 50)     # Ciudad (lista desplegable?)
    cobertura               = models.CharField(max_length=10)    # Distancia de cobertura de envios -> podria ser una lista de barrios o un medidor de distancia desde direccion
    contacto                = models.CharField(max_length=100)    # Lista con mail, telefono, web, instagram, etc
    envio                   = models.CharField(max_length=100)       # envio a cargo del local? costo?
    horarios                = models.CharField(max_length=100)    # disponibilidad para envios
    is_published            = models.BooleanField(default=True)
    active                  = models.BooleanField(default=False)
    # logo = IMAGEN  
    # PRIVATE
    # value
    # opiniones
    owner = models.ForeignKey(CustomUser , on_delete=models.DO_NOTHING)
    featured = models.BooleanField(default=False)
    
    objects = EmprendimientoManager()

    def get_absolute_url(self):
       #return "/emprens/{slug}".format(slug=self.slug)
        return reverse("detail", kwargs={"slug": self.slug})
    def __str__(self):
        return self.nombre  #, self.rubro , self.subrubro , self.barrio , self.ciudad


def emprendimiento_pre_save_receiver(sender , instance , *args , **kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

pre_save.connect(emprendimiento_pre_save_receiver , sender=Emprendimiento)