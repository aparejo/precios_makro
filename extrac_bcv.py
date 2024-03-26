import requests
from datetime import date
from decimal import Decimal
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'precios_makro.settings')

django.setup()

from precios.models import BCV

# Obtener la fecha actual
fecha_actual = date.today().strftime("%d%m%Y")

# URL de la API con la fecha actual
url = f"http://bg.redvital.com/bgapi.php?modulo=POS&funcion=TASA_BCV&fecha={fecha_actual}&moneda=BC%24"

try:
    # Realizar la solicitud HTTP
    response = requests.get(url)
    data = response.json()

    # Obtener el precio de la respuesta y convertirlo a Decimal
    precio = Decimal(data["CAMBIO"])

    # Actualizar el único registro existente en la base de datos
    try:
        bcv = BCV.objects.first()
        bcv.precio = precio
        bcv.fecha = date.today()
        bcv.save()
        print("Se ha actualizado el único registro existente de BCV en la base de datos")
    except BCV.DoesNotExist:
        print("No se encontró ningún registro existente de BCV")

except requests.exceptions.RequestException as e:
    print(f"Error al obtener los datos de la API: {str(e)}")