from django.contrib import admin
from .models import Category,Products,Contact

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','nuevo','categoria']
    list_editable=['precio']
    search_fields=['nombre']
    list_filter=['categoria','nuevo']
    list_per_page=5



admin.site.register(Category)
admin.site.register(Products, ProductoAdmin)
admin.site.register(Contact)