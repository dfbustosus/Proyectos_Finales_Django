from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home-page'),
    path('about/',views.about, name='about'),
]