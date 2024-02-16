from django.contrib import admin
from precios.models import Producto, Sucursal

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion", "pvp_base","referencia")
    search_fields = ['descripcion', 'codigo', 'marca']
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Sucursal)
