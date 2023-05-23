import django
import unittest
from django.test import TestCase

# Import the Django model you want to test.
from AppPreEntreg3.forms import RemerasForm, PantalonesForm, BuzosForm

# Write your unit test(s)
class RemeraFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'Remera233%', 'tamaño': 'LL4', 'color': 'Verde', 'precio': '127.1', 'stock': '1'}
        form = RemerasForm(data=form_data)
        print(form)

    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': 'Remera233%', 'tamaño': 'LL4', 'color': None, 'precio': '127.1', 'stock': '1'}
        form = RemerasForm(data=form_data)
        print(form)

class BuzoFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'Buzo233%', 'tamaño': 'XL1', 'color': 'Gris', 'precio': '19.1', 'stock': '1'}
        form = BuzosForm(data=form_data)
        print(form)

    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': None, 'tamaño': 'LL4', 'color': None, 'precio': '127.1', 'stock': '1'}
        form = BuzosForm(data=form_data)
        print(form)

class PantalonFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'Buzo233%', 'tamaño': 'XL1', 'color': 'Gris', 'diseño': 'CA', 'precio': '19.1', 'stock': '1'}
        form = PantalonesForm(data=form_data)
        print(form)

    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': 'Buzo233%', 'tamaño': 'XL1', 'color': 'Gris', 'diseño': None, 'precio': '19.1', 'stock': '1'}
        form = PantalonesForm(data=form_data)
        print(form)

# Run your unit test(s) with a test runner
if __name__ == '__main__':
    django.setup()
    unittest.main()