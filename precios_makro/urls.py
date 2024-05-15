<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from precios import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from precios.views import agregar_sede, sucursales, agregar_pantalla, pantalla_view, modificar_pantalla, ofertas_view, ofertasp, ofertast, ofertasf, ofertasf0, ofertasf1, ofertasf2,ofertast04_1, ofertast02_1
from precios.views import ofertast16_1, ofertast16_2, ofertast16_3, ofertast16_4, ofertast16_5, ofertast16_6, ofertast16_7, ofertast16_8, crear_rol
from precios.views import verificador_detail, fondos_verificador, crear_verificador,leer_codigo_de_barrasfinal, editar_producto, ofertapos
from precios import views

app_name = 'administradores'
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.BASE, name='BASE'),
    path('crear-rol/', crear_rol, name='crear_rol'),
    path('productos/', views.productos, name='productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('agregar-sede/', agregar_sede, name='agregar_sede'),
    path('agregar-pantalla/', agregar_pantalla, name='agregar_pantalla'),
    path('sucursales/', sucursales, name='sucursales'),
    path('administradores/', views.administradores, name='administradores'),
    path('verificador/<slug:slug>/', verificador_detail, name='verificador_detail'),
    path('verificadores/crear/', crear_verificador, name='crear_verificador'),
    path('fondos/', fondos_verificador, name='fondos_verificador'),
    path('product/<str:codigo>/editar/', editar_producto, name='editar_producto'),
    path('agregar_administrador/', views.agregar_administrador, name='agregar_administrador'),
    path('pantallas/', pantalla_view, name='pantallas'),
    path('ofertas/', ofertas_view, name='ofertas'),
    path('pantallas/<int:pantalla_id>/', views.ver_pantalla, name='ver_pantalla'),
    path('pantallas/<int:pantalla_id>/modificar/', views.modificar_pantalla, name='modificar_pantalla'),
    path('pantallas/<int:pantalla_id>/eliminar/', views.eliminar_pantalla, name='eliminar_pantalla'),
    path('maracay/<str:nombre_pantalla>/', views.mostrar_pantalla_mcy, name='mostrar_pantalla_mcy'),
    path('barras/', views.leer_codigo_de_barras, name='leer_codigo_de_barras'),
    path('barra/<str:id>/', leer_codigo_de_barrasfinal, name='leer_codigo_de_barrasfinal'),
    path('crear_combo/', views.crear_combo, name='crear_combo'),
    path('barras-t30/', views.leer_codigo_de_barrasT30, name='leer_codigo_de_barrasT30'),
    path('barras-t08/', views.leer_codigo_de_barrasT08, name='leer_codigo_de_barrasT08'),
    path('barras-t01/', views.leer_codigo_de_barrasT01, name='leer_codigo_de_barrasT01'),
    path('barras-t03/', views.leer_codigo_de_barrasT30, name='leer_codigo_de_barrasT30'),
    path('barras-t25/', views.leer_codigo_de_barrasT25, name='leer_codigo_de_barrasT25'),
    path('barras-v21/', views.leer_codigo_de_barrasV21, name='leer_codigo_de_barrasV21'),
    path('barras-t24/', views.leer_codigo_de_barrasT24, name='leer_codigo_de_barrasT24'),
    path('ofertasp/', ofertasp, name='ofertasp'),
    path('ofertast/', ofertast, name='ofertast'),
    path('ofertasf/', ofertasf, name='ofertasf'),
    path('ofertapos/', ofertapos, name='ofertapos'),
    path('ofertasf0/', ofertasf0, name='ofertasf0'),
    path('ofertasf1/', ofertasf1, name='ofertasf1'),
    path('ofertasf2/', ofertasf2, name='ofertasf2'),
    path('ofertast04-1/', ofertast04_1, name='ofertast04_1'), # La Limpia
    path('ofertast02-1/', ofertast02_1, name='ofertast02_1'), # Yaguara
    path('ofertast16-1/', ofertast16_1, name='ofertast16_1'), #Charallave
    path('ofertast16-2/', ofertast16_2, name='ofertast16_2'), #Charallave
    path('ofertast16-3/', ofertast16_3, name='ofertast16_3'), #Charallave
    path('ofertast16-4/', ofertast16_4, name='ofertast16_4'), #Charallave
    path('ofertast16-5/', ofertast16_5, name='ofertast16_5'), #Charallave
    path('ofertast16-6/', ofertast16_6, name='ofertast16_6'), #Charallave
    path('ofertast16-7/', ofertast16_7, name='ofertast16_7'), #Charallave
    path('ofertast16-8/', ofertast16_8, name='ofertast16_8'), #Charallave
    path('barras-t05/', views.leer_codigo_de_barrasT05, name='leer_codigo_de_barrasT05'),
    path('barras-v02/', views.leer_codigo_de_barrasV02, name='leer_codigo_de_barrasV02'),
    path('promo/', views.promo, name='promo'),  # Agrega esta línea para la URL 'promo.html'
]
=======
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
from precios.views import agregar_sede, sucursales, agregar_pantalla, pantalla_view, modificar_pantalla, ofertas_view, ofertasp, ofertast, ofertasf, ofertasf0, ofertasf1, ofertasf2,ofertast04_1, ofertast02_1
from precios.views import ofertast16_1, ofertast16_2, ofertast16_3, ofertast16_4, ofertast16_5, ofertast16_6, ofertast16_7, ofertast16_8
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
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
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
    path('barras-t03/', views.leer_codigo_de_barrasT30, name='leer_codigo_de_barrasT30'),
    path('barras-t25/', views.leer_codigo_de_barrasT25, name='leer_codigo_de_barrasT25'),
    path('barras-v21/', views.leer_codigo_de_barrasV21, name='leer_codigo_de_barrasV21'),
    path('barras-t24/', views.leer_codigo_de_barrasT24, name='leer_codigo_de_barrasT24'),
    path('ofertasp/', ofertasp, name='ofertasp'),
    path('ofertast/', ofertast, name='ofertast'),
    path('ofertasf/', ofertasf, name='ofertasf'),
    path('ofertasf0/', ofertasf0, name='ofertasf0'),
    path('ofertasf1/', ofertasf1, name='ofertasf1'),
    path('ofertasf2/', ofertasf2, name='ofertasf2'),
    path('ofertast04-1/', ofertast04_1, name='ofertast04_1'), # La Limpia
    path('ofertast02-1/', ofertast02_1, name='ofertast02_1'), # Yaguara
    path('ofertast16-1/', ofertast16_1, name='ofertast16_1'), #Charallave
    path('ofertast16-2/', ofertast16_2, name='ofertast16_2'), #Charallave
    path('ofertast16-3/', ofertast16_3, name='ofertast16_3'), #Charallave
    path('ofertast16-4/', ofertast16_4, name='ofertast16_4'), #Charallave
    path('ofertast16-5/', ofertast16_5, name='ofertast16_5'), #Charallave
    path('ofertast16-6/', ofertast16_6, name='ofertast16_6'), #Charallave
    path('ofertast16-7/', ofertast16_7, name='ofertast16_7'), #Charallave
    path('ofertast16-8/', ofertast16_8, name='ofertast16_8'), #Charallave
    path('barras-t05/', views.leer_codigo_de_barrasT05, name='leer_codigo_de_barrasT05'),
    path('barras-v02/', views.leer_codigo_de_barrasV02, name='leer_codigo_de_barrasV02'),
    path('promo/', views.promo, name='promo'),  # Agrega esta línea para la URL 'promo.html'
]
>>>>>>> 862a94dadb65376628e7c18dafabd3bc9b537173
