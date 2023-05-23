from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Opinion
from .models import Comentario

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:"" for k in fields}
        
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
    imagen= forms.ImageField(required=True)
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',)
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'contenido': 'Comentario',
        }   
class AvatarFormulario(forms.Form):
    
    
    imagen = forms.ImageField(required=True)



