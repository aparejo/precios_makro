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
from precios.views import agregar_sede, sucursales

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.BASE, name='BASE'),
    path('productos/', views.productos, name='productos'),
    path('agregar-sede/', agregar_sede, name='agregar_sede'),
    path('sucursales/', sucursales, name='sucursales'),
]
