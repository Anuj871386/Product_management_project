from celery import shared_task
import json
from categories.models import Category
from products.models import Product

@shared_task
def process_upload(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for category in data['categories']:
            Category.objects.create(**category)
        for product in data['products']:
            Product.objects.create(**product)
