# Generated by Django 4.2.3 on 2024-04-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0010_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='linea',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
