from django.test import TestCase
from App1.forms import UserRegisterForm,UserEditForm,AvatarFormulario
import django
import unittest
from django import forms
from django.contrib.auth.models import User

class UserRegisterFormTest(unittest.TestCase):
    def test_form_fields(self):
        form = UserRegisterForm()
        self.assertIsInstance(form.fields['email'], forms.EmailField)
        self.assertIsInstance(form.fields['password1'], forms.CharField)
        self.assertIsInstance(form.fields['password2'], forms.CharField)

    def test_form_meta(self):
        form = UserRegisterForm()
        self.assertEqual(form.Meta.model, User)
        self.assertEqual(form.Meta.fields, ['username', 'email', 'password1', 'password2'])
        self.assertEqual(form.Meta.help_texts, {'username': '', 'email': '', 'password1': '', 'password2': ''})

if __name__ == '__main__':
    unittest.main()

class UserEditFormTest(unittest.TestCase):
    def test_form_fields(self):
        form = UserEditForm()
        self.assertIsInstance(form.fields['email'], forms.EmailField)
        self.assertIsInstance(form.fields['password1'], forms.CharField)
        self.assertIsInstance(form.fields['password2'], forms.CharField)
        self.assertIsInstance(form.fields['last_name'], forms.CharField)
        self.assertIsInstance(form.fields['first_name'], forms.CharField)

    def test_form_labels(self):
        form = UserEditForm()
        self.assertEqual(form.fields['email'].label, 'Ingrese su email:')
        self.assertEqual(form.fields['password1'].label, 'Contraseña')
        self.assertEqual(form.fields['password2'].label, 'Repetir la contraseña')

    def test_form_meta(self):
        form = UserEditForm()
        self.assertEqual(form.Meta.model, User)
        self.assertEqual(form.Meta.fields, ['email', 'password1', 'password2', 'last_name', 'first_name'])

if __name__ == '__main__':
    unittest.main()
    
class AvatarFormularioTest(unittest.TestCase):
    def test_form_fields(self):
        form = AvatarFormulario()
        self.assertIsInstance(form.fields['imagen'], forms.ImageField)
    
    def test_form_required(self):
        form = AvatarFormulario()
        self.assertTrue(form.fields['imagen'].required)

if __name__ == '__main__':
    unittest.main()


