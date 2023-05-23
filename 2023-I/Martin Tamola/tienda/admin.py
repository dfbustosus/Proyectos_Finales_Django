from django.contrib import admin
from tienda import models
from .forms import ProductoForm
# Register your models here.


class ProdctoAdmin(admin.ModelAdmin):
    list_display = ['nombre' , 'precio', 'nuevo', 'marca']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_filter = ['marca','nuevo']
    list_per_page = 5
    form = ProductoForm
    
    
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre' , 'correo', 'tipo_consulta', 'mensaje']
    list_filter = ['nombre','tipo_consulta']
    list_per_page = 5

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'avatar']
    

admin.site.register(models.Marca)
admin.site.register(models.Prodcto,ProdctoAdmin)
admin.site.register(models.Contacto,ContactoAdmin)
admin.site.register(models.Profile,ProfileAdmin)