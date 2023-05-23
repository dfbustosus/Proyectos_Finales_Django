from django import forms
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class BlogForm(forms.ModelForm):
    picture = forms.FileField(required=False)
    upload_field_name = 'picture'
    class Meta:
        model = Blog
        fields= ['title', 'subtitle', 'body','author','picture']
    
    def save(self, commit=True):
        instance = super(BlogForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()
            self.save_m2m()

        return instance

# post = BlogForm()
# post.save()
