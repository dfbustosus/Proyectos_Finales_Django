from django.test import TestCase
from .forms import *
from .views import *
import unittest

class MedicinaFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'titulo': 'John', 'subtitulo': 'Doe', 'texto': 'aaaaaa', 'autor': 'unca'}
        form = MiembrosForm(data=form_data)
        print(form)
        #print(self.assertTrue(form.is_valid()))
    def test_invalid_form(self):
        form_data = {'titulo': 'John', 'subtitulo': 'Doe', 'texto': None, 'autor': 'unca'}
        form = MiembrosForm(data=form_data)
        print(form)
        #print(self.assertFalse(form.is_valid()))


class MiembrosUpdateTest(TestCase):
    def test_valid_form(self):
        form_data = {'nombre': 'John', 'apellido': 'Doe', 'email': 'aaaaaa', 'email': 'unca'}
        form = MiembrosForm(data=form_data)
        print(form)

class BiologiaUpdateTest(TestCase):
    def test_valid_form(self):
        form_data = {'titulo': 'John', 'subtitulo': 'Doe', 'texto': 'aaaaaa', 'autor': 'unca'}
        form = MiembrosForm(data=form_data)
        print(form)
    def test_invalid_form(self):
        form_data = {'titulo': 'John', None: 'Doe', 'texto': None, 'autor': 'unca'}
        form = MiembrosForm(data=form_data)
        print(form)




