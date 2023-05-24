from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
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

class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True) 

class UserEditForm(UserCreationForm):
    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
   
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']       

class UserEditForm2(UserCreationForm):
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
       
      

class UserEditForm3(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['username'].disabled = True
        self.fields.pop('password')
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    

class CalificacionFormulario(forms.Form):
    id= forms.IntegerField()
    usuario= forms.CharField(max_length=30)
    fecha=forms.DateField()
    puntaje= forms.CharField(max_length=1)
    comentario= forms.CharField(max_length=140)

class DescripcionFormulario(forms.Form):
    id= forms.IntegerField()
    acerca= forms.CharField(max_length=140)
    
class ContactoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField(label="Ingrese su email:")
    telefono= forms.CharField(max_length=15)
    consulta= forms.CharField(max_length=140)   