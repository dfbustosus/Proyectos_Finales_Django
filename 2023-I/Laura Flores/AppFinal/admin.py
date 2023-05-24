from multiprocessing.connection import Client
from django.contrib import admin
from AppFinal.models import Recipe, Client, Comment
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Client)
admin.site.register(Comment)
