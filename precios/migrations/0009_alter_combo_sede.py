# Generated by Django 4.2.3 on 2024-03-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0008_combo_sede'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='sede',
            field=models.CharField(max_length=100, null=True),
        ),
    ]