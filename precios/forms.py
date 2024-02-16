from django import forms
from .models import Sucursal

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'codigo']