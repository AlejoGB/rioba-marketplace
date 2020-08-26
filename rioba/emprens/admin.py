from django.contrib import admin
from .models import Emprendimiento

class EmprensAdmin(admin.ModelAdmin):
    list_display = ('id' , 'nombre' , 'is_published')
    list_display_links = ('id' , 'nombre')

admin.site.register(Emprendimiento , EmprensAdmin)
# Register your models here.