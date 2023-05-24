from django import forms

class EmpleadoForm(forms.Form):
    dni= forms.IntegerField(label="DNI")
    nombre= forms.CharField(label="Nombre empleado", max_length=50)
    id_departamento= forms.IntegerField(label="Codigo Departamento")
    id_puesto= forms.IntegerField(label="Codigo Puesto")

class DepartamentoForm(forms.Form):
    codigo= forms.IntegerField(label="Codigo")
    nombre= forms.CharField(label="Descripción Departamento", max_length=50)

class PuestoForm(forms.Form):
    codigo= forms.IntegerField(label="Codigo")
    nombre= forms.CharField(label="Descripción Puesto", max_length=50)
    departamento= forms.CharField(label="Departamento", max_length=50)       


  
