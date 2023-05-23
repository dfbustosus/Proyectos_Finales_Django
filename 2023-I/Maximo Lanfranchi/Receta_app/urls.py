from django.urls import path 
from Receta_app import views 

urlpatterns=[
     path('pages/',views.receta_list, name='receta_list'),
    path('create/', views.receta_nuevo, name='receta-nuevo'),
    path('<int:pk>/', views.receta_detail, name='receta-detalle'),
    path('<int:pk>/update/', views.receta_modificar, name='receta-modificar'),
    path('<int:pk>/borrar/', views.confirmar_receta_borrar, name='confirmar-receta-borrar'),
    path('<int:pk>/delete/', views.receta_borrar, name='receta-borrar'),
    path('about/', views.about, name= 'aboutme'),
    path('contacto/', views.contact, name='contacto'),
    path('buscar/', views.receta_buscar, name='receta_buscar'),
]