# Generated by Django 5.0.2 on 2024-03-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0009_alter_combo_sede'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=255)),
                ('subcategoria', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
            ],
        ),
    ]
