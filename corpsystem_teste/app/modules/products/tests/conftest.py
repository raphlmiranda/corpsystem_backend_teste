import pytest
from typing import Dict

@pytest.fixture
def object_data() -> Dict[str, str]:
    return {
        "name": "Produto Teste II",
        "description": "Descrição Teste",
        "price": 100.00,
        "quantity": 10,
        "sku": "SKU-TESTE-02"
    }