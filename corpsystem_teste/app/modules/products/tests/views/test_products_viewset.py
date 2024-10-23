import pytest
from typing import Dict
from django.urls import reverse

from corpsystem_teste.app.modules.products.tests.factories import ProductFactory

@pytest.mark.django_db
class TestProductsViewSet:

    def test_products_list(self, api_client, products: ProductFactory):
        url = reverse("api:products-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_products_list_actives(self, api_client, products: ProductFactory):
        url = reverse("api:products-list")
        response = api_client.get(url, params={"is_active": True})
        assert response.status_code == 200
        assert len(response.data) == 1
    
    def test_products_create_success(self, api_client, object_data: Dict):
        url = reverse("api:products-list")
        response = api_client.post(url, data=object_data)
        assert response.status_code == 201

    def test_products_create_fail_without_param(self, api_client, object_data: Dict):
        url = reverse("api:products-list")
        object_data.pop("sku")
        response = api_client.post(url, data=object_data)
        assert response.status_code == 400

    def test_products_create_fail_with_invalid_quantity(self, api_client, object_data: Dict):
        url = reverse("api:products-list")
        object_data["quantity"] = 0
        response = api_client.post(url, data=object_data)
        assert response.status_code == 400

    def test_products_retrieve(self, api_client, products: ProductFactory):
        url = reverse("api:products-detail", kwargs={"pk": products.pk})
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_products_retrieve_unexisting_product_id(self, api_client):
        url = reverse("api:products-detail", kwargs={"pk": 2})
        response = api_client.get(url)
        assert response.status_code == 404

    def test_products_update_with_invalid_param(self, api_client, products: ProductFactory, object_data: Dict):
        url = reverse("api:products-detail", kwargs={"pk": products.pk})
        response = api_client.patch(url, data=object_data)
        assert response.status_code == 400

    def test_products_update_zero_quantity(self, api_client, products: ProductFactory, object_data: Dict):
        url = reverse("api:products-detail", kwargs={"pk": products.pk})
        object_data.pop("sku")
        object_data["quantity"] = 0
        response = api_client.patch(url, data=object_data)
        assert response.status_code == 200
        assert response.json()["is_active"] == False

    def test_products_update_success(self, api_client, products: ProductFactory, object_data: Dict):
        url = reverse("api:products-detail", kwargs={"pk": products.pk})
        object_data.pop("sku")
        response = api_client.patch(url, data=object_data)
        assert response.status_code == 200
        assert response.json()["is_active"] == True
