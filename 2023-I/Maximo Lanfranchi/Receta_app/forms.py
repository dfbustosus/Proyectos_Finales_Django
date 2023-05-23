from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['title', 'subtitle', 'author', 'description', 'release_date', 'poster']