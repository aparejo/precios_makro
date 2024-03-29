# Generated by Django 4.2.3 on 2024-03-18 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0004_producto_fecha_actualizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantalla',
            name='codigo_barra',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pantalla',
            name='id_producto',
            field=models.ForeignKey(blank=True, db_column='id_producto', null=True, on_delete=django.db.models.deletion.CASCADE, to='precios.producto', to_field='codigo'),
        ),
    ]