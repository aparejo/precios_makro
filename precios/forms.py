from django import forms
from precios.models import Sucursal,Roles
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Pantalla, Producto, Verificador, FondoVerificador
from django.utils.text import slugify

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
    slug = forms.CharField(max_length=200, widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Sucursal
        fields = ['nombre', 'codigo', 'slug']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = self.generate_slug(instance.nombre)
        if commit:
            instance.save()
        return instance

    def generate_slug(self, nombre):
        slug = slugify(nombre)
        slug = slug.replace('-', '_')
        return slug

class AdminForm(UserCreationForm):
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all())
    rol = forms.ModelChoiceField(queryset=Roles.objects.all())

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('sucursal', 'rol')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.sucursal_id = self.cleaned_data['sucursal'].id
        user.roles_id = self.cleaned_data['rol'].id
        if commit:
            user.save()
        return user
    
class RolForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['nombre']
        
class VerificadorForm(forms.ModelForm):
    class Meta:
        model = Verificador
        fields = ['sucursal', 'slug', 'fondo']
        # Puedes personalizar las etiquetas de los campos y agregar estilos de CSS si lo deseas
        labels = {
            'sucursal': 'Sucursal',
            'slug': 'Slug',
            'fondo': 'Fondo',
        }
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # Puedes agregar widgets adicionales para personalizar la apariencia de los campos
        }

class FondoVerificadorForm(forms.ModelForm):
    class Meta:
        model = FondoVerificador
        fields = ['nombre', 'archivo_imagen', 'archivo_css']
        labels = {
            'nombre': 'Nombre',
            'archivo_imagen': 'Archivo de imagen',
            'archivo_css': 'Archivo CSS',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            # Puedes agregar widgets adicionales para personalizar la apariencia de los campos
        }
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'referencia', 'imagen']