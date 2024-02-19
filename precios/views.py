from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Sucursal
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from .forms import SedeForm
from .forms import AdminForm
from .models import Usuario

def administradores(request):
    administradores = Usuario.objects.filter(is_superuser=False)
    return render(request, 'administradores.html', {'administradores': administradores})

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

def sucursales(request):
    sucursales = Sucursal.objects.all()

    return render(request, 'sucursales.html', {'sucursales': sucursales})

def agregar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../..')
    else:
        form = SedeForm()

    return render(request, 'agregar_sede.html', {'form': form})