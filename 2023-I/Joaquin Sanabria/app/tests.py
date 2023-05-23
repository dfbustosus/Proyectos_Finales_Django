from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from .models import Curso, Estudiante
from .forms import EntregableForm,BusquedaForm

class EntregableFormTest(TestCase):

    def setUp(self):
        # Añade los campos necesarios para crear un curso y un estudiante
        self.curso = Curso.objects.create(nombre='Curso de Prueba', descripcion='Este es un curso de prueba')
        self.estudiante = Estudiante.objects.create(nombre='Estudiante de Prueba', edad=20)
        self.archivo = SimpleUploadedFile("archivo.txt", b"file_content", content_type="text/plain")
    
    def test_valid_form(self):
        form_data = {
            'titulo': 'Trabajo Final',
            'descripcion': 'Trabajo final del curso de Python',
            'fecha_entrega': date.today(),
            'curso': self.curso.id,
            'estudiante': self.estudiante.id,
            'archivo': self.archivo
        }
        form = EntregableForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_no_title(self):
        form_data = {
            'titulo': '',
            'descripcion': 'Trabajo final del curso de Python',
            'fecha_entrega': date.today(),
            'curso': self.curso.id,
            'estudiante': self.estudiante.id,
            'archivo': self.archivo
        }
        form = EntregableForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_no_description(self):
        form_data = {
            'titulo': 'Trabajo Final',
            'descripcion': '',
            'fecha_entrega': date.today(),
            'curso': self.curso.id,
            'estudiante': self.estudiante.id,
            'archivo': self.archivo
        }
        form = EntregableForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_no_file(self):
        form_data = {
            'titulo': 'Trabajo Final',
            'descripcion': 'Trabajo final del curso de Python',
            'fecha_entrega': date.today(),
            'curso': self.curso.id,
            'estudiante': self.estudiante.id,
            'archivo': None
        }
        form = EntregableForm(data=form_data)
        self.assertFalse(form.is_valid())


class BusquedaFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'busqueda': 'Python',
            'opcion': 'curso',
        }
        form = BusquedaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_no_busqueda(self):
        form_data = {
            'busqueda': '',
            'opcion': 'curso',
        }
        form = BusquedaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_form_todos_los_cursos(self):
        form_data = {
            'busqueda': '',
            'opcion': 'todos_los_cursos',
        }
        form = BusquedaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_no_option(self):
        form_data = {
            'busqueda': 'Python',
            'opcion': '',
        }
        form = BusquedaForm(data=form_data)
        self.assertFalse(form.is_valid())





