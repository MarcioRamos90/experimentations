# Generated by Django 5.0.4 on 2024-04-23 02:03

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0003_rename_price_products_preço_remove_products_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.CharField(max_length=255, unique=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(blank=True)),
                ("short_description", models.CharField(blank=True, max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("domain", models.CharField(max_length=50, unique=True)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=None,
                        default="products/default.jpg",
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=-1,
                        scale=None,
                        size=[700, 700],
                        upload_to="products/",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("categories", models.ManyToManyField(to="Core.category")),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.DeleteModel(
            name="Products",
        ),
    ]