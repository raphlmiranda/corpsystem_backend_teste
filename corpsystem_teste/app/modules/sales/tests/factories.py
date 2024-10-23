from factory.django import DjangoModelFactory

from app.modules.sales.models import Sale, ENUM_SALE_STATUS


class SaleFactory(DjangoModelFactory):
    
    name = 'Vendas de teste'
    description = 'Vendas de teste para testar o sistema'
    quantity = 2
    status = ENUM_SALE_STATUS.PENDING

    class Meta:
        model = Sale
        django_get_or_create = ['name']
        skip_postgeneration_save = True