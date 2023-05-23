from django.test import TestCase

from App1.forms import ProveedorFormu, ProductoFormu
import django 
# Import the Django model you want to test
from App1.forms import ClienteFormu
import unittest
# Import the Django test framework
from django.test import TestCase

# Write your unit test(s)
class ProveedorFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'Jose', 'apellido': 'Rodriguez', 'email': 'jrodri@gmail.com', 'cuit': 'Developer'}
        form = ProveedorFormu(data=form_data)
        print(form)
        #print(self.assertTrue(form.is_valid()))

    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': 'Jose', 'apellido': 'Rodriguez', 'email': None, 'cuit': 'Developer'}
        form = ProveedorFormu(data=form_data)
        print(form)
        #print(self.assertFalse(form.is_valid()))

# Run your unit test(s) with a test runner
if __name__ == '__main__':
    django.setup()
    unittest.main()