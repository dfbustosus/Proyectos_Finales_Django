from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class CrearPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','subtitulo','contenido','categoria', 'imagen']
        widgets = {
            'titulo':forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo':forms.TextInput(attrs={'class': 'form-control'}),
            'contenido':forms.Textarea(attrs={'class': 'form-control'}),
        }

class ImagenPost(forms.Form):
    imagen = forms.ImageField(required=True)

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'first_name' :forms.TextInput(attrs={'class':'form-control'})
        }


class AvatarFormulario(forms.Form):
    imagen= forms.ImageField(required=True)