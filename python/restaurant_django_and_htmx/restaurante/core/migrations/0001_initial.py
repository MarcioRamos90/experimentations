# Generated by Django 5.0.4 on 2024-04-21 15:00

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("nome", models.CharField(max_length=50, unique=True)),
                ("descrição", models.CharField(blank=True, max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "dominio",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="nome de dominio"
                    ),
                ),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=-1,
                        scale=None,
                        size=[700, 700],
                        upload_to="media/",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
