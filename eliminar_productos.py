import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'precios_makro.settings')
django.setup()

from precios.models import Producto

# Eliminar todos los productos
Producto.objects.all().delete()