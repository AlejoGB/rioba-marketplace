from django.db import models

# Create your models here.
from django.db import models
from emprens.models import Emprendimiento


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image_path(instance , filename):
    new_filename = random.randint(1,154125125)
    name , ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f"emprens/{new_filename}/{final_filename}"

class Producto(models.Model):
    # PUBLIC
    nombre = models.CharField(max_length=50)
    rubro  = models.CharField(max_length=50)       # heredado de emprend definitivamente lista desplegable
    subrubro = models.CharField(max_length=50)     # particular del producto
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to=upload_image_path , null=True , blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    # logo = IMAGEN  
    # PRIVATE
    # value
    # opiniones
    owner = models.ForeignKey(Emprendimiento , on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre #, self.rubro , self.subrubro , self.barrio , self.ciudad