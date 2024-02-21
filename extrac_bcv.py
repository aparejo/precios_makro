import os
import django
import time
import requests
from decimal import Decimal
from json.decoder import JSONDecodeError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'precios_makro.settings')
django.setup()
from precios.models import BCV

def obtener_datos_y_actualizar():
    url = "https://pydolarvenezuela-api.vercel.app/api/v1/dollar/page?page=bcv"

    try:
        response = requests.get(url)
        data = response.json()
        procesar_datos(data)
    except JSONDecodeError as e:
        print("Error al hacer la solicitud:", e)

def procesar_datos(data):
    usd_data = data.get("usd")
    if usd_data:
        precio = Decimal(usd_data.get("price"))
        fecha_str = usd_data.get("datetime", {}).get("date")

        # Verifica si ya existe un registro en la tabla BCV
        try:
            bcv = BCV.objects.get(id=1)
            # Actualiza el campo "precio" y "fecha" del objeto existente
            bcv.precio = precio
            bcv.fecha = fecha_str
            bcv.save()
        except BCV.DoesNotExist:
            # Crea un nuevo objeto BCV
            bcv = BCV(id=1, fecha=fecha_str, precio=precio)
            bcv.save()

while True:
    obtener_datos_y_actualizar()
    # Espera 45 minutos antes de realizar la próxima actualización
    time.sleep(60 * 60)