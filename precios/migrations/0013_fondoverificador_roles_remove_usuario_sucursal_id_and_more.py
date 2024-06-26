# Generated by Django 5.0.2 on 2024-04-11 08:50

import django.db.models.deletion
import precios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0012_oferta_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FondoVerificador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('archivo_imagen', models.ImageField(upload_to='fondos_verificador/')),
                ('archivo_css', models.FileField(blank=True, null=True, upload_to='fondos_verificador_css/')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='sucursal_id',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=precios.models.upload_to),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='precios.sucursal'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='precios.roles'),
        ),
        migrations.CreateModel(
            name='Verificador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('fondo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='precios.fondoverificador')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='precios.sucursal')),
            ],
        ),
    ]
