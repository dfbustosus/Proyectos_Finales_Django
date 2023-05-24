from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen')
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'precio': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nombre', 'descripcion', 'precio', 'imagen', 'vendido')
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'precio': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }