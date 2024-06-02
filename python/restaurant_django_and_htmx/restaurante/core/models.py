from django.db import models
from django_resized import ResizedImageField
from django.utils.html import mark_safe


class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True) 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False, auto_created=True)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=False)
    short_description = models.CharField(max_length=255, blank=True, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
    domain = models.CharField(max_length=50, unique=True, blank=False, null=False)
    image = ResizedImageField(size=[500, 500], blank=True, null=True, upload_to="products/", default="products/default.jpg")
    categories = models.ManyToManyField("Category")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self) -> str:
        return f"<{self.name}>"
    
    def __str__(self) -> str:
        return f"<{self.id} | {self.name} | {self.price}>"
    
    def image_tag(self):
            return mark_safe('<img src="%s" width="100" height="100" />' % (self.image.url))

    image_tag.short_description = 'Image'
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
