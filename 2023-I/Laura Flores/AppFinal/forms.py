from AppFinal.models import Comment, Recipe
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class Client_Form(UserCreationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']

class Recipe_Form(UserCreationForm,forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "time", "ingredients", "directions", "highlight","public", "author","date", "image"]


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments','punctuation','name']

class BusquedaRecetas(forms.Form):
    search = forms.CharField()
