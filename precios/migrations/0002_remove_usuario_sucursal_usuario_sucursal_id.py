# Generated by Django 4.2.3 on 2024-02-19 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='usuario',
            name='sucursal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='precios.sucursal'),
        ),
    ]
