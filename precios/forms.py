from django import forms
from precios.models import Sucursal
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Pantalla, Producto

class BarcodeForm(forms.Form):
    barcode = forms.CharField(max_length=20)

class PantallaForm(forms.ModelForm):
    class Meta:
        model = Pantalla
        fields = ['nombre', 'sucursal', 'descripcion', 'tipo', 'codigo_barra']
        labels = {
            'codigo_barra': 'Código de Barra',
        }
        widgets = {
            'codigo_barra': forms.TextInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        codigo_barra = cleaned_data.get('codigo_barra')

        if not codigo_barra:
            raise forms.ValidationError('Debe proporcionar un código de barra.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        if instance.codigo_barra:
            producto = Producto.objects.filter(barra=instance.codigo_barra).first()
            if producto:
                instance.id_producto = producto
                instance.descripcion = producto.descripcion

        if commit:
            instance.save()

        return instance


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'codigo']


class AdminForm(UserCreationForm):
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all())

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('sucursal',)