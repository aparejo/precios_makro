import requests
from datetime import datetime
from decimal import Decimal
import django
import os
import dateparser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "precios_makro.settings")
django.setup()
from precios.models import BCV

def procesar_datos():
    url = "https://pydolarvenezuela-api.vercel.app/api/v1/dollar/page?page=bcv"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hay errores en la respuesta HTTP

        data = response.json()
        
        usd_data = data.get("monitors", {}).get("usd")
        
        if usd_data:
            precio_str = usd_data.get("price")
            precio = Decimal(precio_str)
            
            # Formatear el precio con cuatro decimales
            precio_formateado = "{:.4f}".format(precio)
            fecha_str = data.get("datetime", {}).get("date")
            fecha = dateparser.parse(fecha_str)

            # Verifica si ya existe un registro en la tabla precios_bcv
            try:
                bcv = BCV.objects.get(id=1)
                # Actualiza el campo "precio" y "fecha" del objeto existente
                bcv.precio = precio_formateado
                bcv.fecha = fecha
                bcv.save()
            except BCV.DoesNotExist:
                # Crea un nuevo objeto precios_bcv
                bcv = BCV(id=1, fecha=fecha, precio=precio_formateado)
                bcv.save()
            print(precio_formateado)  # Imprime el precio formateado con cuatro decimales   
    except requests.exceptions.RequestException as e:
        print("Error al obtener los datos del API:", str(e))
    
    except Exception as e:
        print("Error desconocido:", str(e))

procesar_datos()