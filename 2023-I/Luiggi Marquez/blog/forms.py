from django.forms import ModelForm
from .models import Posts
from django import forms
from ckeditor.fields import RichTextFormField

class PostsForm(ModelForm):

    title = forms.CharField(label= 'Título', required=True, widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    subtitle = forms.CharField(label= 'Descripción', required=True, widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100)
    Message = RichTextFormField()
    imageMain = forms.ImageField(label = 'Imagen', required=True, widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Posts
        fields =['title','subtitle','Message','imageMain']

class PostsEditForm(ModelForm):

    title = forms.CharField(label= 'Título', required=True, widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100)
    subtitle = forms.CharField(label= 'Descripción', required=True, widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100)
    Message = RichTextFormField(label="Publicación", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    imageMain = forms.ImageField(label = 'Imagen', required=True)
    delete_image = forms.BooleanField(required=False, initial=False, label='Eliminar imagen existente')

    class Meta:
        model = Posts
        fields =['title','subtitle','Message','imageMain', 'delete_image']
