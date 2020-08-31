from django.contrib import admin
from .models import Emprendimiento , Producto

class EmprensAdmin(admin.ModelAdmin):
    list_display = ('id' , 'nombre' , 'is_published')
    list_display_links = ('id' , 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id' , 'nombre' , 'emprendimiento' , 'stock')
    list_display_links = ('id' , 'nombre')

admin.site.register(Emprendimiento , EmprensAdmin)
admin.site.register(Producto, ProductoAdmin)
# Register your models here.