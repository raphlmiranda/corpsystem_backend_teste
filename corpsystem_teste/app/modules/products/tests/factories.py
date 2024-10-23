from factory.django import DjangoModelFactory

from corpsystem_teste.app.modules.products.models import Product


class ProductFactory(DjangoModelFactory):

    name = 'Produto I'
    description = 'Descrição do produto I'
    price = 100.00
    image_url = 'https://i.imgur.com/000000000000.jpg'
    quantity = 10
    sku = 'SKU-TESTE-1'


    class Meta:
        model = Product
        django_get_or_create = ['sku']
        skip_postgeneration_save = True
    