# Generated by Django 4.2.3 on 2024-02-27 13:58

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('barra', models.CharField(max_length=20)),
                ('referencia', models.CharField(max_length=50)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('catalogo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=50)),
                ('sub_marca', models.CharField(max_length=50)),
                ('um', models.CharField(max_length=20)),
                ('linea', models.CharField(max_length=20)),
                ('desc_linea', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
                ('desc_categoria', models.CharField(max_length=50)),
                ('sub_categoria', models.CharField(max_length=20)),
                ('desc_sub_categoria', models.CharField(max_length=50)),
                ('existencia_total', models.CharField(max_length=20)),
                ('pvp_base', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('la_Urbina', models.CharField(default='N/A', max_length=8)),
                ('la_Urbina_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('la_Yaguara', models.CharField(default='N/A', max_length=8)),
                ('la_Yaguara_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('San_Diego', models.CharField(default='N/A', max_length=8)),
                ('San_Diego_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('La_Limpia', models.CharField(default='N/A', max_length=8)),
                ('La_Limpia_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Barquisimeto', models.CharField(default='N/A', max_length=8)),
                ('Barquisimeto_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Turmero', models.CharField(default='N/A', max_length=8)),
                ('Turmero_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Cristal', models.CharField(default='N/A', max_length=8)),
                ('Cristal_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Charallave', models.CharField(default='N/A', max_length=8)),
                ('Charallave_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('La_Guaira', models.CharField(default='N/A', max_length=8)),
                ('La_Guaira_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Lisandro', models.CharField(default='N/A', max_length=8)),
                ('Lisandro_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Rio_Lama', models.CharField(default='N/A', max_length=8)),
                ('Rio_Lama_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Santa_Teresa', models.CharField(default='N/A', max_length=8)),
                ('Santa_Teresa_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Guarenas', models.CharField(default='N/A', max_length=8)),
                ('Guarenas_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Guacara', models.CharField(default='N/A', max_length=8)),
                ('Guacara_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('La_Vina', models.CharField(default='N/A', max_length=8)),
                ('La_Vina_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Puerto_Cabello', models.CharField(default='N/A', max_length=8)),
                ('Puerto_Cabello_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Los_Teques', models.CharField(default='N/A', max_length=8)),
                ('Los_Teques_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Ocumare_Tuy', models.CharField(default='N/A', max_length=8)),
                ('Ocumare_Tuy_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Guaparo', models.CharField(default='N/A', max_length=8)),
                ('Guaparo_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Maracay', models.CharField(default='N/A', max_length=8)),
                ('Maracay_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
                ('Barra2', models.CharField(default=None, max_length=20, null=True)),
                ('Barra2_pvp', models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pantalla',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('vertical', 'Pantalla vertical'), ('horizontal', 'Pantalla horizontal')], max_length=10)),
                ('id_producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='precios.producto', to_field='codigo')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='precios.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_name='usuarios', to='auth.group')),
                ('sucursal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='precios.sucursal')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuarios', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
