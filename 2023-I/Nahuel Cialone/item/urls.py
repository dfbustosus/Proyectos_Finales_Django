from django.urls import path
from . import views

#recordar el nombre de esta app para poder agregarlo a urls del proyecto principal
app_name = 'item'

urlpatterns = [
    #incluyendo int:pk, el path espera el id del item para desplegar el view de detalles
    path('', views.items, name='items'),
    path('nuevo/', views.new, name='new'),
    path('<int:pk>/', views.detalle, name='detalle'),
    path('<int:pk>/editar', views.edit, name='editar'),
    path('<int:pk>/borrar', views.delete, name='borrar'),
]