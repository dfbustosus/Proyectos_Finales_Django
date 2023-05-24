from django import forms
from .models import *




class MiembrosForm(forms.ModelForm):
    class Meta:
        model = Miembros
        fields = ['nombre', 'apellido', 'email', 'universidad', 'foto']
        widgets = {'foto': forms.FileInput()}

class MedicinaForm(forms.ModelForm):
    class Meta:
        model = Medicina
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

class BiologiaForm(forms.ModelForm):
    class Meta:
        model = Biología
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

class FilosofiaForm(forms.ModelForm):
    class Meta:
        model = Filosofía
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}
    
class AstronomiaForm(forms.ModelForm):
    class Meta:
        model = Astronomía
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnología
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
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
    
    imagen = forms.ImageField(required=True)





