from django import forms

class RegistroUsuario(forms.Form):
    id=forms.IntegerField()
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.EmailField()
    contraseña=forms.CharField(max_length=20)


class ComprasUsuariof(forms.Form):
    id=forms.IntegerField()
    usuario=forms.CharField(max_length=20)
    producto=forms.CharField(max_length=20)
    cantidad=forms.IntegerField()


class stocklista(forms.Form):
    id=forms.IntegerField()
    producto=forms.CharField(max_length=30)
    cantidad=forms.IntegerField()
    precio=forms.IntegerField()
