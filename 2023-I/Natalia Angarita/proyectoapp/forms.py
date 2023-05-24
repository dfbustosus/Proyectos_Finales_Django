from django import forms
 
class productoFormulario(forms.Form):
    id= forms.IntegerField()
    categoria = forms.CharField()
    nombre = forms.CharField()
    precio = forms.IntegerField()
    
class clienteFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class vendedorFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    categoria= forms.CharField(max_length=30)