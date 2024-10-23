import pytest
from typing import Dict

@pytest.fixture
def object_data() -> Dict[str, str]:
    return {
        "name": "Client Test",
        "email": "client@test.com",
        "phone": "99999999999",
        "cpf": "97264424006",
        "address": "Address Test",
    }