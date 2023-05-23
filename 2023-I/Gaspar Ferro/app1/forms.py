from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class cursoformulario(forms.Form):
    nombre = forms.CharField()
    raza = forms.CharField()

class Creacionformulario(forms.Form):
    nombre = forms.CharField (max_length=30)
    genero = forms.CharField (max_length=30)
    profesion = forms.CharField (max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class LoginForm(forms.Form):
    usuario = forms.CharField (max_length=30)
    password = forms.CharField (max_length=30)



