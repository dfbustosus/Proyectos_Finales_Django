from django.test import TestCase

from .models import Receta

# Create your tests here.
from django.test import TestCase

from recetas_app.forms import RecetaForm
import django 
import unittest
import unittest
from django.test import TestCase

from recetas_app.forms import RecetaForm
import django 
# Import the Django model you want to test
from auth_app.forms import CustomAuthenticationForm, CustomUserCreationForm
import unittest
# Import the Django test framework
from django.test import TestCase

class CustomAuthenticationForm(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'John', 'apellido': 'Doe', 'email': 'john.doe@example.com', 'profesion': 'Developer'}
        form = CustomAuthenticationForm(data=form_data)
        print(form)
        #print(self.assertTrue(form.is_valid()))

    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': 'John', 'apellido': 'Doe', 'email': None, 'profesion': 'Developer'}
        form = CustomAuthenticationForm(data=form_data)
        print(form)
        #print(self.assertFalse(form.is_valid()))

# Run your unit test(s) with a test runner
if __name__ == '__main__':
    django.setup()
    unittest.main()

