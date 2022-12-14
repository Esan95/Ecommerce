from django import forms
from .models import EjemploormProductos

class ProductoForm(forms.ModelForm):

    class Meta:
        model = EjemploormProductos
        fields = '__all__'