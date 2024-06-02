from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "domain", "price", "created_at", "updated_at", "image_tag"]
    list_display_links = ["id", "name", "domain"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    list_display_links = ["id", "name"]

    

