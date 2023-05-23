from django.contrib import admin
from .models import Clients
from .models import Products
from .models import Sellers

# Register your models here.
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Sellers)
