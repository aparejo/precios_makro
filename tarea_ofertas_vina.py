from django.db.models import F
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'precios_makro.settings')
django.setup()
from precios.models import Producto, Oferta

def actualizar_ofertas():
    # Eliminar todas las ofertas existentes
    Oferta.objects.all().delete()

    # Obtener los productos que cumplen el filtro
    productos = Producto.objects.filter(la_Urbina_pvp__lt=F('pvp_base'))

    # Crear ofertas basadas en los productos filtrados
    for producto in productos:
        print("Procesando producto:", producto.descripcion)

        oferta = Oferta()
        oferta.titulo = producto.descripcion
        oferta.imagen = 'productos/imagenes_png/{}.png'.format(producto.codigo)
        oferta.precio = producto.la_Urbina_pvp
        oferta.categoria = producto.desc_categoria
        oferta.subcategoria = producto.desc_sub_categoria
        oferta.marca = producto.marca
        oferta.save()

        print("Oferta creada:", oferta.titulo)

    print("Actualización de ofertas completada.")