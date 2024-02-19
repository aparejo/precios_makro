from django import forms
from precios.models import Sucursal
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Pantalla

class PantallaForm(forms.ModelForm):
    class Meta:
        model = Pantalla
        fields = ['nombre', 'sucursal', 'descripcion', 'tipo', 'id_producto']


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'codigo']


class AdminForm(UserCreationForm):
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all())

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('sucursal',)