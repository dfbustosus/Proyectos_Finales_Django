from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.contrib.auth import get_user

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Usuario", max_length=20,required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Nombre", max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:

        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields}

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este Email ya esta siendo usado")
        return email


class editUserForm(UserCreationForm):


    email = forms.EmailField(label = "Modificar Email", required = False,)
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Introduce nuevo Password'}), required = False)
    password2 = forms.CharField(label = "Repite Contraseña", widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repite nuevo Password'}), required = False)
    first_name = forms.CharField(label = "Nombre", required = False)
    last_name = forms.CharField(label = "Apellido", required = False) 

    class Meta():
        model = User
        fields = ['email','password1','password2','first_name','last_name']

        helps_text = {k:"" for k in fields}

    def clean_email(self):
        
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists() and (email != self.user.email): #Para poder lanza la excepcion, debe ser un mail que ya exista en el DB pero que no sea el mail actual del login
            raise forms.ValidationError("Este Email ya esta siendo usado")
        return email

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user')
        super(editUserForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'value':self.user.email, 'class':'form-control', 'placeholder':'Introduce nuevo Email'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'value':self.user.first_name, 'class':'form-control', 'placeholder':'Introduce nuevo Nombre'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'value':self.user.last_name, 'class':'form-control', 'placeholder':'Introduce nuevo Apellido'})
        
    