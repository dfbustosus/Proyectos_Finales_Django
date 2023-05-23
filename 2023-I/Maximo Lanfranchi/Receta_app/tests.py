from django.test import TestCase

# Create your tests here.
from Receta_app.forms import RecetaForm
import django 
import unittest


class RecetaFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'title': 'Super Milanesa', 
                     'subtitle': 'Unas milanesas Increibles!', 
                     'author': 'John the chef', 
                     'description': 'Para empezar con la receta de milanesa de carne, primero debes sazonar la carne con la sal, la pimienta y el orégano al gusto. Luego, pasa cada uno de los filetes de ternera por el pan rallado que necesites (por ambos lados)....',
                     'release_date': '10/10/2023'
                     }
        form = RecetaForm(data=form_data)
        print(form)
        #print(self.assertTrue(form.is_valid()))

    def test_invalid_form(self): 
        form_data = {'title': 'Super Milanesa', 
                     'subtitle': 'Unas milanesas Increibles!', 
                     'author': 'John the chef', 
                     'description': 'Para empezar con la receta de milanesa de carne, primero debes sazonar la carne con la sal, la pimienta y el orégano al gusto. Luego, pasa cada uno de los filetes de ternera por el pan rallado que necesites (por ambos lados)....',
                     'release_date': '202313-13',
                     'poster': '/panes.jpg'}
        form = RecetaForm(data=form_data)
        print(form)
        #print(self.assertFalse(form.is_valid()))

# Run your unit test(s) with a test runner
if __name__ == '__main__':
    django.setup()
    unittest.main()