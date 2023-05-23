from django import forms
from AppPreEntreg3.models import choicesPant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RemerasForm(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=3)
    color = forms.CharField(max_length=10)
    precio = forms.FloatField()
    stock = forms.IntegerField()

class BuzosForm(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=3)
    color = forms.CharField(max_length=10)
    precio = forms.FloatField()
    stock = forms.IntegerField()

class PantalonesForm(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=3)
    color = forms.CharField(max_length=10)
    diseño = forms.ChoiceField(choices=choicesPant)
    precio = forms.FloatField()
    stock = forms.IntegerField()

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
    imagen = forms.ImageField(required=True)  #Subimos un avatar como usuario.
