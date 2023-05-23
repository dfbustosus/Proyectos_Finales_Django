from django import forms
from .models import Clients, Products, Sellers, Avatar
 
class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'sku', 'image']

class SellerForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = ['name', 'email']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)