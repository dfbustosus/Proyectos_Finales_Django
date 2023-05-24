from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('contenido',)
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
            
        }