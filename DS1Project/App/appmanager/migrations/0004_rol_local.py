# Generated by Django 4.2.5 on 2023-11-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appmanager", "0003_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rol_local",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=20)),
                ("description", models.TextField(default="", max_length=100)),
            ],
        ),
    ]
