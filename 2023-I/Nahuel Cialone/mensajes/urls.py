from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detalle, name='detalle'),
    path('nuevo/<int:item_pk>/', views.nueva_conversacion, name='nuevo'),
]