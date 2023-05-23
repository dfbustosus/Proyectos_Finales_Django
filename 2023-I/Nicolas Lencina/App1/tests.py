from django.test import TestCase, Client

from django import forms 
from App1.forms import ProductoFormulario , UserRegisterForm
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import unittest

# Create your tests here.
from django.test import TestCase
from .forms import ProductoFormulario

class ProductoFormularioTest(TestCase):
    def test_producto_formulario_valido(self):
        form_data = {
            'id': 1,
            'nombre': 'Producto 1',
            'codigodeventa': 12345,
            'descripcion': 'Descripción del producto',
            
            # Agrega los demás campos según corresponda
        }
        form = ProductoFormulario(data=form_data)
        print(form)

    def test_producto_formulario_codigodeventa_invalido(self):
        form_data = {
            'id': 2,
            'nombre': 'Producto 2',
            'codigodeventa': 'invalido',
            'descripcion': 'Descripción del producto',
           
        }
        form = ProductoFormulario(data=form_data)
        
        print(form)

class UserRegisterFormTest(TestCase):
    def test_userregister_valido(self):
        form_data = {
            'username': 'valido',
            'email': 'valido@gmail.com',
            'password1': '3265987N',
            'password2': '3265987N',
        }
        form = UserRegisterForm(data=form_data)
        
        print(form)
    
    def test_userregister_invalido(self):
        form_data = {
            'username': 'valido',
            'email': 'validogmail.com',
            'password1': '3265987N',
            'password2': '3265987N',
        }
        form = UserRegisterForm(data=form_data)
        
        print(form)


from django.urls import reverse


class ProductoCreacionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_creacion_producto(self):
        url = reverse('New')  # Reemplaza 'nombre_de_la_url' con el nombre real de la URL definida en urls.py
        response = self.client.post(url, {'nombre': 'Producto de prueba', 'codigodeventa': '12345'})
        print(response)
        self.assertEqual(response.status_code, 302)  # Verifica que la respuesta sea un redireccionamiento (código 302)
        self.assertRedirects(response, '/App1/producto/list')

class ProductoCreacionTestCase2(TestCase):
    def setUp(self):
        self.client = Client()
        self.invalid_data = {
            'nombre': '',  # Campo vacío, lo cual es inválido
            'codigodeventa': '12345'
        }

    def test_producto_creacion_invalid(self):
        url = reverse('New')  # Obtener la URL de la vista usando el nombre definido en urls.py
        response = self.client.post(url, self.invalid_data)
        self.assertEqual(response.status_code, 200)  # Verificar que la respuesta tiene el código 200
        self.assertFormError(response, 'form', 'nombre', 'Este campo es obligatorio.')  # Verificar el error de validación del campo 'nombre'