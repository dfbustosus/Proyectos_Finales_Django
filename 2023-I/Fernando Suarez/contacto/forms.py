from django import forms

class formularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True, max_length=50)
    email=forms.CharField(label="eMail", required=True, max_length=50)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)
