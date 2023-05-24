
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views
#recordar el nombre de esta app para poder agregarlo a urls del proyecto principal
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]