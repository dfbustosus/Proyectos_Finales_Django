from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App1.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'description', 'website')