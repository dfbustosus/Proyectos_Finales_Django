from django.test import TestCase
from AnatoApp.forms import EntradaForm, AsistenciasFormulario

class EntradaFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'titulo': 'Huesos', 'subtitulo': 'MMSS', 'cuerpo': 'mensaje a desarrollar'}
        form = EntradaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'titulo': ' ', 'subtitulo': 'MMSS', 'cuerpo': 'mensaje a desarrollar'}
        form = EntradaForm(data=form_data)
        self.assertFalse(form.is_valid())


class AsistenciaFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'nombre': 'Bautista', 'comision': '8', 'clase': 'Huesos del carpo','presente': True}
        form = AsistenciasFormulario(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'nombre': 'Bautista', 'comision': '8', 'clase': 'Huesos del carpo','presente': False}
        form = AsistenciasFormulario(data=form_data)
        self.assertFalse(form.is_valid())
