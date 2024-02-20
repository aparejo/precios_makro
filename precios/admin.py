from django.contrib import admin
from django.contrib import admin
from precios.models import Producto, Sucursal, Usuario, Pantalla

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion", "pvp_base","referencia")
    search_fields = ['descripcion', 'codigo', 'marca']
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Sucursal)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Pantalla)
class PantallaAdmin(admin.ModelAdmin):
    pass