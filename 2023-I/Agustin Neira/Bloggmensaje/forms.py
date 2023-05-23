from django import forms
from django.contrib.auth.models import User
from datetime import datetime

class MensajeForm(forms.Form):
    receptor = forms.ChoiceField(label='Receptor', choices=[(user.username, user.username) for user in User.objects.all()],)    
    mensaje = forms.CharField(label="cuerpo", widget=forms.Textarea,)
    fecha = forms.DateTimeField(label="fecha", initial=datetime.now())

