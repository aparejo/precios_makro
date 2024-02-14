import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "precios_makro.settings")
django.setup()

from precios.models import Producto

# Obtén todos los objetos Producto de la base de datos
productos = Producto.objects.all()

# Identifica los códigos repetidos
codigos_repetidos = []
codigos_vistos = set()

for producto in productos:
    if producto.codigo in codigos_vistos:
        codigos_repetidos.append(producto.codigo)
    else:
        codigos_vistos.add(producto.codigo)

# Elimina los objetos Producto con códigos repetidos
for codigo_repetido in codigos_repetidos:
    Producto.objects.filter(codigo=codigo_repetido).delete()

print("Se han eliminado los códigos repetidos.")