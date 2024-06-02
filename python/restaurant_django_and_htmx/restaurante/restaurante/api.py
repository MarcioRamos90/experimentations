from typing import List
import urllib.parse
import urllib.request
from ninja import NinjaAPI, Schema

from core.models import Product as ProductModel, Category as CategoryModel
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib


api = NinjaAPI()


class ProductSchema(Schema):
    name: str
    price: float
    description: str
    domain: str
    categories: List[str]
    image: str = None


class CategorySchema(Schema):
    name: str


class DataSchema(Schema):
    products: List[ProductSchema]
    categories: List[CategorySchema]


@api.post("/import_data")
def import_product(request, data: DataSchema):
    created_count = []
    error_count = []
    for item in data.products:
        try:
            product_object_model = get_by_domain(item.domain)
            if not product_object_model:
                product_object_model = create_product(item)

            attach_image(product_object_model, item.image)
                
            # cache to use categories already retrieved
            categories_retrieved_cache = {}

            get_or_create_categories(data, categories_retrieved_cache)

            for category_object_model in categories_retrieved_cache:
                if categories_retrieved_cache[category_object_model].name in item.categories:
                    add_category_to_product(categories_retrieved_cache[category_object_model], product_object_model)

            created_count.append([product_object_model.id, product_object_model.name])
        except Exception as e:
            error_count.append([item.name, str(e)])

    return {"created_successfully": created_count, "failed_to_create": error_count}


def get_by_domain(domain):
    return ProductModel.objects.filter(domain = domain).first()


def attach_image(product_object_model: ProductModel, image):
    if image:
        with urllib.request.urlopen(image) as f:
            img_temp = NamedTemporaryFile()
            img_temp.write(f.read())
            img_temp.flush()
            product_object_model.image.save(image.split("\\")[-1], File(img_temp))


def create_product(item):
        product_object_model = ProductModel(
            name = item.name,
            description = item.description,
            short_description = item.description[0:100],
            price = item.price,
            domain = item.domain,
        )
        product_object_model.save()

        return product_object_model

def add_category_to_product(category_object_model, product_object_model: ProductModel):
    product_object_model.categories.add(category_object_model)


def get_or_create_categories(data, categories_retrieved_cache):
    # retrieve and/or create categories
    for category_item in data.categories:
        # get from previously retrieved categories
        c = categories_retrieved_cache.get(category_item.name)
        
        if not c:
            # find category in database 
            c = CategoryModel.objects.filter(name = category_item.name).first()

        if not c:
            # create category
            c = CategoryModel(name = category_item.name)
            c.save()
        
        categories_retrieved_cache[category_item.name] = c