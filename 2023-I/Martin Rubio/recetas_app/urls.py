from django.urls import path
from . import views

urlpatterns = [
    path('', views.receta_list, name='recetas-page'),
    path('create/', views.receta_new, name='receta-create'),
    path('<int:pk>/', views.receta_detail, name='receta-detail'),
    path('<int:pk>/update/', views.receta_edit, name='receta-update'),
    path('<int:pk>/delete/', views.receta_delete, name='receta-delete'),
]
