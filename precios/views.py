from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Sucursal
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from .forms import SedeForm
from .forms import AdminForm, BarcodeForm
from precios.models import Usuario, Pantalla,BCV
from .forms import PantallaForm, Pantalla 

from decimal import Decimal

def leer_codigo_de_barras(request):
    context = {}
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            try:
                producto = Producto.objects.get(barra=barcode)
                precio_bcv = BCV.objects.get(id=1).precio  # Obtener el precio del BCV
                pvp_base = producto.pvp_base * Decimal(precio_bcv)  # Realizar la multiplicación
                context['producto'] = producto
                context['pvp_base_bcv'] = pvp_base  # Agregar el resultado al contexto
            except Producto.DoesNotExist:
                context['error'] = 'El código de barras no está asociado a ningún producto.'
            except BCV.DoesNotExist:
                context['error'] = 'No se encontró el precio del BCV.'
    else:
        form = BarcodeForm()
        context['form'] = form

    return render(request, 'validador_precios_vina.html', context)

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
    return render(request, 'base.html')

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