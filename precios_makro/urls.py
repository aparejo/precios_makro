"""
URL configuration for precios_makro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from precios import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from precios.views import agregar_sede, sucursales, agregar_pantalla, pantalla_view, modificar_pantalla, ofertas_view
from precios import views

app_name = 'administradores'
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.BASE, name='BASE'),
    path('productos/', views.productos, name='productos'),
    path('agregar-sede/', agregar_sede, name='agregar_sede'),
    path('agregar-pantalla/', agregar_pantalla, name='agregar_pantalla'),
    path('sucursales/', sucursales, name='sucursales'),
    path('administradores/', views.administradores, name='administradores'),
    path('agregar_administrador/', views.agregar_administrador, name='agregar_administrador'),
    path('pantallas/', pantalla_view, name='pantallas'),
    path('ofertas/', ofertas_view, name='ofertas'),
    path('pantallas/<int:pantalla_id>/', views.ver_pantalla, name='ver_pantalla'),
    path('pantallas/<int:pantalla_id>/modificar/', views.modificar_pantalla, name='modificar_pantalla'),
    path('pantallas/<int:pantalla_id>/eliminar/', views.eliminar_pantalla, name='eliminar_pantalla'),
    path('maracay/<str:nombre_pantalla>/', views.mostrar_pantalla_mcy, name='mostrar_pantalla_mcy'),
    path('barras/', views.leer_codigo_de_barras, name='leer_codigo_de_barras'),
    path('crear_combo/', views.crear_combo, name='crear_combo'),
    path('barras-t30/', views.leer_codigo_de_barrasT30, name='leer_codigo_de_barrasT30'),
    path('barras-t08/', views.leer_codigo_de_barrasT08, name='leer_codigo_de_barrasT08'),
    path('barras-t25/', views.leer_codigo_de_barrasT25, name='leer_codigo_de_barrasT25'),
    path('barras-v21/', views.leer_codigo_de_barrasV21, name='leer_codigo_de_barrasV21'),
    path('barras-t24/', views.leer_codigo_de_barrasT24, name='leer_codigo_de_barrasT24'),
]
