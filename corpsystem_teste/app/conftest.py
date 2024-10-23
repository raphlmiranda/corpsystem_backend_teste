import pytest
from rest_framework.test import APIClient

from corpsystem_teste.app.modules.clients.tests.factories import ClientFactory
from corpsystem_teste.app.modules.products.tests.factories import ProductFactory


@pytest.fixture
def clients():
    return ClientFactory(
        id=1,
        name='Client Test',
        email='client@test.com',
        phone='99999999999',
        cpf='99999999999',
        address='Address Test'
    )

@pytest.fixture
def products():
    return ProductFactory(
        id=1,
        name='Product Test',
        description='Description Test',
        price=100.00,
        image_url='https://i.imgur.com/000000000000.jpg',
        quantity=10,
        sku='SKU-TESTE-1'
    )

@pytest.fixture
def api_client():
    return APIClient()