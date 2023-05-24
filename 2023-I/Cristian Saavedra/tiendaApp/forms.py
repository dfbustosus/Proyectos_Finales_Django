from django import forms
from django.forms import fields, widgets
from .models import Category,Products,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'

        widgets={

            'fecha_fabricacion':forms.SelectDateWidget()
        }


class ContactoForm(forms.ModelForm):

    class Meta:
        model=Contact
        #fields=['nombre','correo','tipo_consulta','mensaje','avisos'] otro camino es con __all__
        fields='__all__'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        #fields = ['username', 'email', 'password1', 'password2']
        fields = ['username','password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
