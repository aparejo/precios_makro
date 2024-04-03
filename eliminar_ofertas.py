import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'precios_makro.settings')
django.setup()

from precios.models import Oferta

# Eliminar todos los productos
Oferta.objects.all().delete()