from django import forms
 
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoFormulario(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'codigodeventa','descripcion', 'imagen']

    def clean_id(self):
        id = self.cleaned_data['id']
        if Producto.objects.filter(id=id).exists():
            raise forms.ValidationError('El ID ya está en uso')
        return id
    


    


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