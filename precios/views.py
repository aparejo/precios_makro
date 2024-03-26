from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Sucursal
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from .forms import SedeForm
from .forms import AdminForm, BarcodeForm
from precios.models import Usuario, Pantalla, BCV
from .forms import PantallaForm, Pantalla
from precios.models import TareaActualizacion
from django.utils import timezone
from django.db.models import F

from decimal import Decimal, ROUND_DOWN
from django.http import JsonResponse

def obtener_detalles_producto(request, codigo_barras):
    producto = Producto.objects.get(barra=codigo_barras)
    detalles = {
        'nombre': producto.descripcion,
        'codigo_producto': producto.codigo,
    }
    return JsonResponse(detalles)

def leer_codigo_de_barras(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                # Buscar el producto por el campo "barra"
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                
                #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Realizar la multiplicación
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                # Ajustar el número de decimales a dos
                pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                pvp_base_bcv = round(pvp_base, 2)
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                #context['pvp_base'] = producto.La_Vina_pvp
                context['pvp_base'] = producto.pvp_base
            except Producto.DoesNotExist:
                try:
                    # Buscar el producto por el campo "BARRA_ADIC_COD_1"
                    producto = Producto.objects.get(Q(Barra2=barcode) | Q(barra=barcode))
                    if producto.Barra2:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = Decimal(producto.Barra2_pvp)
                        pvp_base = Preciousd * Decimal(precio_bcv)  # Tomar el precio de Barra2_pvp
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                    else:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = producto.pvp_base
                        pvp_base = Preciousd * Decimal(precio_bcv)
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                        #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Tomar el precio de pvp_base
                        #Preciousd = producto.La_Vina_pvp
                    context['producto'] = producto
                    context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                    context['pvp_base'] = Preciousd
                except Producto.DoesNotExist:
                    context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form
    #return render(request, 'precios_vina.html', context)
    return render(request, 'validador_precios_vina2.html', context)

def leer_codigo_de_barrasT30(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                # Buscar el producto por el campo "barra"
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                
                #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Realizar la multiplicación
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                # Ajustar el número de decimales a dos
                pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                pvp_base_bcv = round(pvp_base, 2)
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                #context['pvp_base'] = producto.La_Vina_pvp
                context['pvp_base'] = producto.pvp_base
            except Producto.DoesNotExist:
                try:
                    # Buscar el producto por el campo "BARRA_ADIC_COD_1"
                    producto = Producto.objects.get(Q(Barra2=barcode) | Q(barra=barcode))
                    if producto.Barra2:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = Decimal(producto.Barra2_pvp)
                        pvp_base = Preciousd * Decimal(precio_bcv)  # Tomar el precio de Barra2_pvp
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                    else:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = producto.pvp_base
                        pvp_base = Preciousd * Decimal(precio_bcv)
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                        #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Tomar el precio de pvp_base
                        #Preciousd = producto.La_Vina_pvp
                    context['producto'] = producto
                    context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                    context['pvp_base'] = Preciousd
                except Producto.DoesNotExist:
                    context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form
    #return render(request, 'precios_vina.html', context)
    return render(request, 'validador_precios_maracay.html', context)

def leer_codigo_de_barrasT08(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                # Buscar el producto por el campo "barra"
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.get(id=2).precio  # Obtener el precio del BCV
                
                #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Realizar la multiplicación
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                # Ajustar el número de decimales a dos
                pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                pvp_base_bcv = round(pvp_base, 2)
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                #context['pvp_base'] = producto.La_Vina_pvp
                context['pvp_base'] = producto.pvp_base
            except Producto.DoesNotExist:
                try:
                    # Buscar el producto por el campo "BARRA_ADIC_COD_1"
                    producto = Producto.objects.get(Q(Barra2=barcode) | Q(barra=barcode))
                    if producto.Barra2:
                        precio_bcv = BCV.objects.get(id=1).precio  # Obtener el precio del BCV
                        Preciousd = Decimal(producto.Barra2_pvp)
                        pvp_base = Preciousd * Decimal(precio_bcv)  # Tomar el precio de Barra2_pvp
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                    else:
                        precio_bcv = BCV.objects.get(id=1).precio  # Obtener el precio del BCV
                        Preciousd = producto.pvp_base
                        pvp_base = Preciousd * Decimal(precio_bcv)
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                        #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Tomar el precio de pvp_base
                        #Preciousd = producto.La_Vina_pvp
                    context['producto'] = producto
                    context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                    context['pvp_base'] = Preciousd
                except Producto.DoesNotExist:
                    context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form
    #return render(request, 'precios_vina.html', context)
    return render(request, 'validador_precios_turmero.html', context)

def leer_codigo_de_barrasT25(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                # Buscar el producto por el campo "barra"
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                
                #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Realizar la multiplicación
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                # Ajustar el número de decimales a dos
                pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                pvp_base_bcv = round(pvp_base, 2)
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                #context['pvp_base'] = producto.La_Vina_pvp
                context['pvp_base'] = producto.pvp_base
            except Producto.DoesNotExist:
                try:
                    # Buscar el producto por el campo "BARRA_ADIC_COD_1"
                    producto = Producto.objects.get(Q(Barra2=barcode) | Q(barra=barcode))
                    if producto.Barra2:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = Decimal(producto.Barra2_pvp)
                        pvp_base = Preciousd * Decimal(precio_bcv)  # Tomar el precio de Barra2_pvp
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                    else:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = producto.pvp_base
                        pvp_base = Preciousd * Decimal(precio_bcv)
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                        #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Tomar el precio de pvp_base
                        #Preciousd = producto.La_Vina_pvp
                    context['producto'] = producto
                    context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                    context['pvp_base'] = Preciousd
                except Producto.DoesNotExist:
                    context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form
    #return render(request, 'precios_vina.html', context)
    return render(request, 'validador_precios_losteques.html', context)

def leer_codigo_de_barrasV21(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                # Buscar el producto por el campo "barra"
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                
                #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Realizar la multiplicación
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                # Ajustar el número de decimales a dos
                pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                pvp_base_bcv = round(pvp_base, 2)
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                #context['pvp_base'] = producto.La_Vina_pvp
                context['pvp_base'] = producto.pvp_base
            except Producto.DoesNotExist:
                try:
                    # Buscar el producto por el campo "BARRA_ADIC_COD_1"
                    producto = Producto.objects.get(Q(Barra2=barcode) | Q(barra=barcode))
                    if producto.Barra2:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = Decimal(producto.Barra2_pvp)
                        pvp_base = Preciousd * Decimal(precio_bcv)  # Tomar el precio de Barra2_pvp
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                    else:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = producto.pvp_base
                        pvp_base = Preciousd * Decimal(precio_bcv)
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                        #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Tomar el precio de pvp_base
                        #Preciousd = producto.La_Vina_pvp
                    context['producto'] = producto
                    context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                    context['pvp_base'] = Preciousd
                except Producto.DoesNotExist:
                    context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form
    #return render(request, 'precios_vina.html', context)
    return render(request, 'validador_precios_guaparo.html', context)

def leer_codigo_de_barrasT24(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                # Buscar el producto por el campo "barra"
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                
                #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Realizar la multiplicación
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                # Ajustar el número de decimales a dos
                pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                pvp_base_bcv = round(pvp_base, 2)
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                #context['pvp_base'] = producto.La_Vina_pvp
                context['pvp_base'] = producto.pvp_base
            except Producto.DoesNotExist:
                try:
                    # Buscar el producto por el campo "BARRA_ADIC_COD_1"
                    producto = Producto.objects.get(Q(Barra2=barcode) | Q(barra=barcode))
                    if producto.Barra2:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = Decimal(producto.Barra2_pvp)
                        pvp_base = Preciousd * Decimal(precio_bcv)  # Tomar el precio de Barra2_pvp
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                    else:
                        precio_bcv = BCV.objects.latest('id').precio  # Obtener el precio del BCV
                        Preciousd = producto.pvp_base
                        pvp_base = Preciousd * Decimal(precio_bcv)
                        pvp_base_bcv = round(pvp_base, 2)
                        pvp_base = pvp_base.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
                        #pvp_base = producto.La_Vina_pvp * Decimal(precio_bcv)  # Tomar el precio de pvp_base
                        #Preciousd = producto.La_Vina_pvp
                    context['producto'] = producto
                    context['pvp_base_bcv'] = pvp_base_bcv  # Agregar el resultado al contexto
                    context['pvp_base'] = Preciousd
                except Producto.DoesNotExist:
                    context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form
    #return render(request, 'precios_vina.html', context)
    return render(request, 'validador_precios_ptocabello.html', context)

def mostrar_pantalla_mcy(request, nombre_pantalla):
    pantalla = Pantalla.objects.filter(nombre=nombre_pantalla).first()

    context = {
        'pantalla': pantalla,
    }
    return render(request, 'monitor-mcy.html', context)

@login_required
def pantalla_view(request):
    pantallas = Pantalla.objects.all()
    return render(request, 'pantallas.html', {'pantallas': pantallas})

@login_required
def ver_pantalla(request, pantalla_id):
    pantalla = get_object_or_404(Pantalla, id=pantalla_id)
    producto = pantalla.id_producto
    return render(request, 'ver_pantalla.html', {'pantalla': pantalla, 'producto': producto})

@login_required
def modificar_pantalla(request, pantalla_id):
    pantalla = get_object_or_404(Pantalla, id=pantalla_id)
    if request.method == 'POST':
        form = PantallaForm(request.POST, instance=pantalla)
        if form.is_valid():
            form.save()
            return redirect('ver_pantalla', pantalla_id=pantalla_id)
    else:
        form = PantallaForm(instance=pantalla)
    return render(request, 'modificar_pantalla.html', {'form': form, 'pantalla': pantalla})

@login_required
def ofertas_view(request):
    productos_oferta = Producto.objects.filter(la_Urbina_pvp__lt=F('pvp_base'))
    # Resto del código de la vista...
    return render(request, 'precios_oferta.html', {'productos_oferta': productos_oferta})


def eliminar_pantalla(request, pantalla_id):
    pantalla = get_object_or_404(Pantalla, id=pantalla_id)
    if request.method == 'POST':
        # Eliminar la pantalla de la base de datos
        pantalla.delete()
        return redirect('lista_pantallas')
    else:
        return render(request, 'eliminar_pantalla.html', {'pantalla': pantalla})

@login_required
def agregar_pantalla(request):
    if request.method == 'POST':
        form = PantallaForm(request.POST)
        if form.is_valid():
            pantalla = form.save(commit=False)
            pantalla.save()
            return redirect('pantallas')  # Redirigir a la página de pantallas
    else:
        form = PantallaForm()
    return render(request, 'agregar_pantalla.html', {'form': form})

@login_required
def administradores(request):
    administradores = Usuario.objects.filter(is_superuser=False)
    return render(request, 'administradores.html', {'administradores': administradores})

@login_required
def agregar_administrador(request):
    form = AdminForm()

    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administradores')

    return render(request, 'agregar_administrador.html', {'form': form})

@login_required
def BASE(request):
    bcv = BCV.objects.order_by('-fecha').first()  # Obtener el último registro
    precio_bcv = bcv.precio if bcv else None  # Obtener el precio o None si no hay registros
    fecha_bcv = bcv.fecha.strftime("%d/%m/%Y") if bcv else None  # Obtener la fecha formateada o None si no hay registros
    cantidad_ofertas = Producto.objects.filter(la_Urbina_pvp__lt=F('pvp_base')).count()

    # Obtener las últimas 5 tareas de actualización
    ultimas_tareas = TareaActualizacion.objects.order_by('-fecha_actualizacion')[:5]

    # Obtener la hora actual del servidor
    hora_actual = timezone.now().strftime("%H:%M:%S")
    
    context = {
        'precio_bcv': precio_bcv,
        'fecha_bcv': fecha_bcv,
        'ultimas_tareas': ultimas_tareas,
        'Ofertas': cantidad_ofertas,
        'hora_actual': hora_actual  # Agregar la hora actual al contexto
    }
    return render(request, 'base.html', context)

@login_required
def productos(request):
    query = request.GET.get('q')
    productos_list = Producto.objects.all()

    if query:
        productos_list = productos_list.filter(
            Q(descripcion__icontains=query) |
            Q(barra__icontains=query) |
            Q(codigo__icontains=query)
        )

    paginator = Paginator(productos_list, 23)

    page = request.GET.get('page', 1)
    try:
        productos = paginator.page(page)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    return render(request, 'productos.html', {'productos': productos, 'paginator': paginator})

@login_required
def sucursales(request):
    sucursales = Sucursal.objects.all()

    return render(request, 'sucursales.html', {'sucursales': sucursales})

@login_required
def agregar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../..')
    else:
        form = SedeForm()

    return render(request, 'agregar_sede.html', {'form': form})