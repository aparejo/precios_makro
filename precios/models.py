from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=100)
    barra = models.CharField(max_length=20)
    referencia = models.CharField(max_length=50)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    catalogo = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    sub_marca = models.CharField(max_length=50)
    um = models.CharField(max_length=20)
    linea = models.CharField(max_length=20)
    desc_linea = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    desc_categoria = models.CharField(max_length=50)
    sub_categoria = models.CharField(max_length=20)
    desc_sub_categoria = models.CharField(max_length=50)
    existencia_total = models.CharField(max_length=20)
    pvp_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    la_Urbina = models.CharField(max_length=8, default='N/A')
    la_Urbina_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    la_Yaguara = models.CharField(max_length=8, default='N/A')
    la_Yaguara_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    San_Diego = models.CharField(max_length=8, default='N/A')
    San_Diego_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    La_Limpia = models.CharField(max_length=8, default='N/A')
    La_Limpia_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Barquisimeto = models.CharField(max_length=8, default='N/A')
    Barquisimeto_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Turmero = models.CharField(max_length=8, default='N/A')
    Turmero_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Cristal = models.CharField(max_length=8, default='N/A')
    Cristal_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Charallave = models.CharField(max_length=8, default='N/A')
    Charallave_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    La_Guaira = models.CharField(max_length=8, default='N/A')
    La_Guaira_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Lisandro = models.CharField(max_length=8, default='N/A')
    Lisandro_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Rio_Lama = models.CharField(max_length=8, default='N/A')
    Rio_Lama_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Santa_Teresa = models.CharField(max_length=8, default='N/A')
    Santa_Teresa_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Guarenas = models.CharField(max_length=8, default='N/A')
    Guarenas_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Guacara = models.CharField(max_length=8, default='N/A')
    Guacara_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    La_Vina = models.CharField(max_length=8, default='N/A')
    La_Vina_pvp = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Puerto_Cabello=models.CharField(max_length=8, default='N/A')
    Puerto_Cabello_pvp=models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Los_Teques=models.CharField(max_length=8, default='N/A')
    Los_Teques_pvp=models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Ocumare_Tuy=models.CharField(max_length=8, default='N/A')
    Ocumare_Tuy_pvp=models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Guaparo=models.CharField(max_length=8, default='N/A')
    Guaparo_pvp=models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Maracay=models.CharField(max_length=8, default='N/A')
    Maracay_pvp=models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    Barra2=models.CharField(max_length=20, null=True, default='N/A')
    Barra2_pvp = models.CharField(max_length=50, null=True, default=None)
    
    def __str__(self):
        return f"{self.descripcion} - {self.codigo} - {self.marca} - {self.pvp_base}"

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    sucursal_id = models.ForeignKey(Sucursal, null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(Group, related_name='usuarios', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        related_name='usuarios',
        blank=True,
        help_text='Specific permissions for this user.',
        )
    
    def __str__(self):
        return self.username
    
class Pantalla(models.Model):
    TIPO_CHOICES = (
        ('vertical', 'Pantalla vertical'),
        ('horizontal', 'Pantalla horizontal'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, to_field='codigo', db_column='id_producto')

    def __str__(self):
        return self.nombre
    
class BCV(models.Model):
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"Fecha: {self.fecha}, Precio: {self.precio}"