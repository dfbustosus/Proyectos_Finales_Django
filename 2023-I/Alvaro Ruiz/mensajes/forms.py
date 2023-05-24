from django.forms import ModelForm
from .models import *

class CrearMensajeForm(ModelForm):
    class Meta:
        model = Mensajeria
        fields = ['mensaje']