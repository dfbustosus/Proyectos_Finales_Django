from django import forms
from .models import Mensaje, User

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']