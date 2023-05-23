from django import forms
 
class ProductoFormu(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    cantidad = forms.IntegerField()

class ClienteFormu(forms.Form):
    id= forms.IntegerField()   
    nombre = forms.CharField()
    apellido = forms.CharField()
    email= forms.CharField()

class ProveedorFormu(forms.Form):
    id= forms.IntegerField()   
    nombre = forms.CharField()
    apellido = forms.CharField()
    email= forms.CharField()
    cuil= forms.IntegerField()   

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True)