import os
import django
import time
import requests
from json.decoder import JSONDecodeError
from django.utils import timezone
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'precios_makro.settings')
django.setup()
from precios.models import Producto
from precios.models import TareaActualizacion

url = "http://bg.redvital.com/bgapi.php?modulo=INV&funcion=LISTA_DE_PRECIOS&codigo_desde=C00060001&codigo_hasta=C00076218"

def obtener_datos_y_actualizar():
    try:
        response = requests.get(url)
        data = response.json()
        procesar_datos(data)
    except JSONDecodeError as e:
        print("Error al decodificar la respuesta JSON:", e)
        
def finalizar_tarea_actualizacion(nombre_tarea):
    tarea = TareaActualizacion(nombre_tarea=nombre_tarea, fecha_actualizacion=timezone.now())
    tarea.save()

def procesar_datos(data):
    with transaction.atomic():
        items = data["items"]
        for item_data in items:
            codigo = item_data["CODIGO"]

            # Verifica si el código ya existe en la base de datos
            try:
                producto = Producto.objects.get(codigo=codigo)
                # Actualiza los campos necesarios del objeto existente
                producto.existencia_total = item_data["EXIS_TOTAL"]
                producto.pvp_base = item_data["PVP_BASE"]
                producto.la_Urbina = item_data["T01_EXIS"]
                producto.la_Urbina_pvp = item_data["T01_PVP"]
                producto.la_Yaguara = item_data["T02_EXIS"]
                producto.la_Yaguara_pvp = item_data["T02_PVP"]
                producto.San_Diego = item_data["T03_EXIS"]
                producto.San_Diego_pvp = item_data["T03_PVP"]
                producto.La_Limpia = item_data["T04_EXIS"]
                producto.La_Limpia_pvp = item_data["T04_PVP"]
                producto.Barquisimeto = item_data["T05_EXIS"]
                producto.Barquisimeto_pvp = item_data["T05_PVP"]
                producto.Turmero = item_data["T08_EXIS"]
                producto.Turmero_pvp = item_data["T08_PVP"]
                producto.Cristal = item_data["T09_EXIS"]
                producto.Cristal_pvp = item_data["T09_PVP"]
                producto.Charallave = item_data["T16_EXIS"]
                producto.Charallave_pvp = item_data["T16_PVP"]
                producto.La_Guaira = item_data["T27_EXIS"]
                producto.La_Guaira_pvp = item_data["T27_PVP"]
                producto.Lisandro = item_data["V01_EXIS"]
                producto.Lisandro_pvp = item_data["V01_PVP"]
                producto.Rio_Lama = item_data["V02_EXIS"]
                producto.Rio_Lama_pvp = item_data["V02_PVP"]
                producto.Santa_Teresa = item_data["V08_EXIS"]
                producto.Santa_Teresa_pvp = item_data["V08_PVP"]
                producto.Guarenas = item_data["V09_EXIS"]
                producto.Guarenas_pvp = item_data["V09_PVP"]
                producto.Guacara = item_data["V11_EXIS"]
                producto.Guacara_pvp = item_data["V11_PVP"]
                producto.La_Vina = item_data["V13_EXIS"]
                producto.La_Vina_pvp = item_data["V13_PVP"]
                producto.Puerto_Cabello=item_data["T24_EXIS"]
                producto.Puerto_Cabello_pvp=item_data["T24_PVP"]
                producto.Los_Teques=item_data["T25_EXIS"],
                producto.Los_Teques_pvp=item_data["T25_PVP"]
                producto.Ocumare_Tuy=item_data["V20_EXIS"]
                producto.Ocumare_Tuy_pvp=item_data["V20_PVP"]
                producto.Guaparo=item_data["V21_EXIS"]
                producto.Guaparo_pvp=item_data["V21_PVP"]
                producto.Maracay=item_data["T30_EXIS"]
                producto.Maracay_pvp=item_data["T30_PVP"]
                producto.Barra2 = item_data["BARRA_ADIC_COD_1"]
                producto.Barra2_pvp = item_data["BARRA_ADIC_PVP_1"]
                producto.fecha_actualizacion = timezone.now()  # Agrega esta línea
                producto.save()
            except Producto.DoesNotExist:
                # Crea un nuevo objeto Producto
                tu_modelo = Producto(
                codigo=codigo,
                    descripcion=item_data["DESCRIPCION"],
                    barra=item_data["BARRA"],
                    referencia=item_data["REFERENCIA"],
                    iva=item_data["IVA"],
                    catalogo=item_data["CATALOGO"],
                    marca=item_data["MARCA"],
                    sub_marca=item_data["SUB_MARCA"],
                    um=item_data["UM"],
                    linea=item_data["LINEA"],
                    desc_linea=item_data["DESC_LINEA"],
                    categoria=item_data["CATEGORIA"],
                    desc_categoria=item_data["DESC_CATEGORIA"],
                    sub_categoria=item_data["SUB_CATEGORIA"],
                    desc_sub_categoria=item_data["DESC_SUB_CATEGORIA"],
                    existencia_total=item_data["EXIS_TOTAL"],
                    pvp_base=item_data["PVP_BASE"],
                    la_Urbina=item_data["T01_EXIS"],
                    la_Urbina_pvp=item_data["T01_PVP"],
                    la_Yaguara=item_data["T02_EXIS"],
                    la_Yaguara_pvp=item_data["T02_PVP"],
                    San_Diego=item_data["T03_EXIS"],
                    San_Diego_pvp=item_data["T03_PVP"],
                    La_Limpia=item_data["T04_EXIS"],
                    La_Limpia_pvp=item_data["T04_PVP"],
                    Barquisimeto=item_data["T05_EXIS"],
                    Barquisimeto_pvp=item_data["T05_PVP"],
                    Turmero=item_data["T08_EXIS"],
                    Turmero_pvp=item_data["T08_PVP"],
                    Cristal=item_data["T09_EXIS"],
                    Cristal_pvp=item_data["T09_PVP"],
                    Charallave=item_data["T16_EXIS"],
                    Charallave_pvp=item_data["T16_PVP"],
                    La_Guaira=item_data["T27_EXIS"],
                    La_Guaira_pvp=item_data["T27_PVP"],
                    Lisandro=item_data["V01_EXIS"],
                    Lisandro_pvp=item_data["V01_PVP"],
                    Rio_Lama=item_data["V02_EXIS"],
                    Rio_Lama_pvp=item_data["V02_PVP"],
                    Santa_Teresa=item_data["V08_EXIS"],
                    Santa_Teresa_pvp=item_data["V08_PVP"],
                    Guarenas=item_data["V09_EXIS"],
                    Guarenas_pvp=item_data["V09_PVP"],
                    Guacara=item_data["V11_EXIS"],
                    Guacara_pvp=item_data["V11_PVP"],
                    La_Vina=item_data["V13_EXIS"],
                    La_Vina_pvp=item_data["V13_PVP"], 
                    Puerto_Cabello=item_data["T24_EXIS"],
                    Puerto_Cabello_pvp=item_data["T24_PVP"],
                    Los_Teques=item_data["T25_EXIS"],
                    Los_Teques_pvp=item_data["T25_PVP"],
                    Ocumare_Tuy=item_data["V20_EXIS"],
                    Ocumare_Tuy_pvp=item_data["V20_PVP"],
                    Guaparo=item_data["V21_EXIS"],
                    Guaparo_pvp=item_data["V21_PVP"],
                    Maracay=item_data["T30_EXIS"],
                    Maracay_pvp=item_data["T30_PVP"],
                    Barra2=item_data["BARRA_ADIC_COD_1"],
                    Barra2_pvp=item_data["BARRA_ADIC_PVP_1"],
                    fecha_actualizacion = timezone.now(),
                )
                tu_modelo.save()
finalizar_tarea_actualizacion("Actualización de productos C5")
obtener_datos_y_actualizar()


