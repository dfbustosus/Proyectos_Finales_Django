from django import forms
 
class GastoFormulario(forms.Form):
    id= forms.IntegerField() 
    fecha= forms.DateField() 
    renta= forms.IntegerField()
    alimentacion= forms.IntegerField()
    educacion= forms.IntegerField()
    transporte= forms.IntegerField()    
    bills= forms.IntegerField()
    vestuario= forms.IntegerField()
    recreacion= forms.IntegerField()  
    otros= forms.IntegerField()

class IngresoFormulario(forms.Form):
    id= forms.IntegerField()
    fecha= forms.DateField()
    salario= forms.IntegerField()
    part_time= forms.IntegerField()
    alquileres= forms.IntegerField()    
    otros= forms.IntegerField() 

class TradingFormulario(forms.Form):
    id= forms.IntegerField()
    fecha= forms.DateField()
    cryptocurrency= forms.IntegerField()
    acciones= forms.IntegerField()
    otros= forms.IntegerField()

###funcion para registrarnos
###user register
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

###funcion para crear usuarios
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

#### AGREGAR un form para obtener un avatar:
class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True)