from django import template

register = template.Library()

@register.filter
def get_cantidad(producto, slug):
    atributo_cantidad = f"{slug}"
    return getattr(producto, atributo_cantidad)

@register.filter
def get_precio(producto, slug):
    atributo_precio = f"{slug}_pvp"
    return getattr(producto, atributo_precio)