from django.test import TestCase
import django 
import unittest
from AppEntrega.forms import *

class RecetaFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 10, 'nombre': 'Agua panela con limon', 'ingredientes': 'Agua, panela y limón', 'descripcion':'Mezclar todos los ingredientes y servir fría'}
        form = RecetaFormulario(data=form_data)
        print(form)
        
class NewsLetterFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1256, 'nombre': 'Maria', 'email':'ejemplo@maria.com'}
        form = NewsLetterFormulario(data=form_data)
        print(form)
        
        
        
if __name__ == '__main__':
    django.setup()
    unittest.main()