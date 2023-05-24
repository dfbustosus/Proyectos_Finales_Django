from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog-page'),
    path('create/', views.blog_new, name='blog-create'),
    path('<int:pk>/', views.blog_detail, name='blog-detail'),
    path('<int:pk>/update/', views.blog_edit, name='blog-update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog-delete'),
    path('about/', views.about, name='about'),
]
