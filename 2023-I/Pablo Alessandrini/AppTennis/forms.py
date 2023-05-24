from django import forms
from .models import Torneo, Jugador,Resultado, Inscripcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# creo los formularios que me van a permitir cargar datos mediante la pagina 
class TorneoFormulario(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    cantidad_jugadores = forms.IntegerField(min_value=1)
    
    class Meta:
        model = Torneo
        fields = '__all__'
        
class JugadorFormulario(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.CharField(max_length=10)
    edad = forms.IntegerField(min_value=1)
    telefono = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=144, initial='')   
    comentario = forms.CharField(widget=forms.Textarea, initial='')
    class Meta:
        model = Jugador
        fields = '__all__'
    
class ResultadoFormulario(forms.ModelForm):
    torneo = forms.ModelChoiceField(queryset=Torneo.objects.all())
    jugador1 = forms.ModelChoiceField(queryset=Jugador.objects.all())
    jugador2 = forms.ModelChoiceField(queryset=Jugador.objects.all())
    resultado = forms.CharField(max_length=50)
    comentario = forms.CharField(max_length=144)
    
    def clean(self):
        cleaned_data = super().clean()
        jugador1 = cleaned_data.get("jugador1")
        jugador2 = cleaned_data.get("jugador2")
        
        if jugador1 == jugador2:
            raise forms.ValidationError("Los jugadores deben ser diferentes")
    class Meta:
        model = Resultado
        fields = '__all__'

class InscripcionFormulario(forms.ModelForm):
    torneo = forms.ModelChoiceField(queryset=Torneo.objects.all())
    jugador = forms.ModelChoiceField(queryset=Jugador.objects.all())
    class Meta:
        model = Inscripcion
        fields ='__all__' 
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': "",
            'email': "",
            'password1': "",
            'password2': "",
        }

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Ingrese su email: ")
    password1=forms.CharField(label="Contraseña: ", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput )
    last_name=forms.CharField()
    first_name=forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    
    
