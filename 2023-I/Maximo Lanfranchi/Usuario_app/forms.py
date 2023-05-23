from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


#Autenicar
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    class Meta:
        fields = ('username', 'password')
        model = User

#Creacion
class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-4'}
        )
    )

    class Meta:
        fields = ('email', 'username', 'password1', 'password2')
        model = User
        #Mensajes de ayuda
        help_texts = {k: "" for k in fields}

#Editar
class CustomUserEditForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control mb-4'}
        )
    )
    webpage = forms.URLField(
        widget=forms.URLInput(
            attrs={'class': 'form-control mb-4'}
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-4'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-4'}
        )
    )

    class Meta:
        fields = ('first_name', 'last_name', 'description',
                  'webpage', 'email', 'password1', 'password2')
        model = User

        #Mensajes de ayuda
        help_texts ={k: "" for k in fields}


class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True)


class CustomAvatarEditForm(forms.Form):
    imagen = forms.ImageField( 
        widget= forms.FileInput(
            attrs= {'class': 'form-control mb-4'}
        )
    )