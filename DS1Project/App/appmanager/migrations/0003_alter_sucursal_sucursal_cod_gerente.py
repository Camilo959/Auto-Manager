# Generated by Django 4.2.6 on 2023-11-18 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmanager', '0002_remove_personaxcargo_perxcargo_rol_cod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='sucursal_cod_gerente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
