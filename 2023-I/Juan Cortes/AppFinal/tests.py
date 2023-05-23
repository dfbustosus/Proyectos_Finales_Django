from django.test import TestCase
from .forms import *
import django
import unittest

#Caso de Prueba #1
#registrar un usuario sin ingresar su email

    #Formulario creado con sus campos requeridos
class UsuarioFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'Pancracio', 'email':'pancracio123@gmail.com', 'telefono':3228539702}
        form = UsuarioFormulario(data=form_data)
        print(form)

    #En esta prueba nos va a dar error ya que el email es un campo requerido para el formulario
    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': 'Pancracio', 'email':None, 'telefono':3228539702}
        form = UsuarioFormulario(data=form_data)
        print(form)

#Resultados: el codigo falla ya que al registrar el usuario sin un email, este no puede proceder a registrarlo ya que es un campo requerido del form

#python manage.py test AppFinal.tests.UsuarioFormularioTest
#python manage.py test AppFinal.tests.UsuarioFormularioTest.test_valid_form
#python manage.py test AppFinal.tests.UsuarioFormularioTest.test_invalid_form


#Caso de Prueba #2
#Registrar un vehiculo en la base de datos con numeros negativos en el modelo del vehiculo

class VehiculoFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'marca': 'Ferrari', 'tipo': 'Deportivo', 'modelo':2018, 'precio': 2000 }
        form = VehiculoFormulario(data=form_data)
        print(form)

    #Numeros negativos en el modelo del vehiculo
    def test_invalid_form(self):
        form_data = {'id': 1, 'marca': 'Ferrari', 'tipo': 'Deportivo', 'modelo': -2020, 'precio': 2000}
        form = VehiculoFormulario(data=form_data)
        print(form)

#Resultados el formulario ignora los numeros negativos y registra el modelo del vehiculo con numeros negativos

#python manage.py test AppFinal.tests.VehiculoFormularioTest
#python manage.py test AppFinal.tests.VehiculoFormularioTest.test_valid_form
#python manage.py test AppFinal.tests.VehiculoFormularioTest.test_invalid_form

#Caso de Prueba #3
#Registrar un comentario en la base de datos, pero con puntos y numero negativo en el telefono del usuario

class ComentarioFormularioTest(TestCase):

    def test_valid_form(self):
        form_data = {'id': 1, 'nombre':'Luciana', 'email':'Luciana1234@gmail.com', 'telefono':3102937897, 'texto':'texto de prueba' }
        form = ComentarioFormulario(data=form_data)
        print(form)
    
    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre':'Luciana', 'email':'Luciana1234@gmail.com', 'telefono': -310.2937897, 'texto':'texto de prueba' }
        form = ComentarioFormulario(data=form_data)
        print(form)


#Resultados: el formulario nos manda un error de que tiene que ingresar un numero completo ya que el punto y el negativo afectan la sintaxis que el formulario admite en el campo de telefono, por ende no permite registrar el usuario

#python manage.py test AppFinal.tests.ComentarioFormularioTest
#python manage.py test AppFinal.tests.ComentarioFormularioTest.test_valid_form
#python manage.py test AppFinal.tests.ComentarioFormularioTest.test_invalid_form

if __name__ == '__main__':
    django.setup()
    unittest.main()




