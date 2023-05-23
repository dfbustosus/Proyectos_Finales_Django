from django import forms 

class RecetaFormulario(forms.Form):
    id=forms.IntegerField()
    nombre = forms.CharField()
    ingredientes = forms.CharField()
    descripcion =forms.CharField()

    
class NewsLetterFormulario(forms.Form):
    id=forms.IntegerField()
    nombre = forms.CharField()
    email =forms.EmailField()
    
    

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