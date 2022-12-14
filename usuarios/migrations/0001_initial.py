# Generated by Django 4.1 on 2022-11-19 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                ("nombre_usuario", models.CharField(max_length=30, unique=True)),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=30)),
                ("correo", models.EmailField(max_length=254, unique=True)),
                ("hash_contraseña", models.CharField(max_length=200)),
            ],
        ),
    ]
