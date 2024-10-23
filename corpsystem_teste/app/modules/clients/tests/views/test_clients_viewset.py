import pytest
from typing import Dict
from django.urls import reverse

from corpsystem_teste.app.modules.clients.tests.factories import ClientFactory

@pytest.mark.django_db
class TestClientsViewSet:

    def test_clients_list(self, api_client):
        url = reverse("api:clients-list")
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_clients_create_success(self, api_client, object_data: Dict):
        url = reverse("api:clients-list")
        response = api_client.post(url, data=object_data)
        assert response.status_code == 201

    def test_clients_create_fail_without_param(self, api_client, object_data: Dict):
        url = reverse("api:clients-list")
        object_data.pop("name")
        response = api_client.post(url, data=object_data)
        assert response.status_code == 400

    def test_clients_create_fail_with_invalid_cpf(self, api_client, object_data: Dict):
        url = reverse("api:clients-list")
        object_data["cpf"] = "12345678901"
        response = api_client.post(url, data=object_data)
        assert response.status_code == 400

    def test_clients_retrieve(self, api_client, clients: ClientFactory):
        url = reverse("api:clients-detail", kwargs={"pk": clients.pk})
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_clients_retrieve_unexisting_client_id(self, api_client):
        url = reverse("api:clients-detail", kwargs={"pk": 2})
        response = api_client.get(url)
        assert response.status_code == 404

    def test_clients_update_fail_with_cpf(self, api_client, clients: ClientFactory, object_data: Dict):
        url = reverse("api:clients-detail", kwargs={"pk": clients.pk})
        response = api_client.patch(url, data=object_data)
        assert response.status_code == 400

    def test_clients_update_success(self, api_client, clients: ClientFactory, object_data: Dict):
        url = reverse("api:clients-detail", kwargs={"pk": clients.pk})
        object_data.pop("cpf")
        response = api_client.patch(url, data=object_data)
        assert response.status_code == 200
