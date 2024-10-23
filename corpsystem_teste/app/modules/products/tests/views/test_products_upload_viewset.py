import pytest
import pandas as pd
from io import BytesIO
from django.urls import reverse

from corpsystem_teste.app.modules.products.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductsUploadViewset:

    def test_upload_products(self, api_client, product_factory: ProductFactory):

        file_data = {
            "name": ["Product 1", "Product 2"],
            "description": ["Description 1", "Description 2"],
            "price": [100.00, 200.00],
            "sku": ["SKU001", "SKU002"],
            "quantity": [10, 20],
        }
        df = pd.DataFrame(file_data)

        excel_file = BytesIO()
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)

        url = reverse("products:upload")
        response = api_client.post(url, data={"file": excel_file}, format="multipart")

        assert response.status_code == 201
        assert response.data["message"] == "Produtos importados com sucesso."
    
    def test_upload_products_without_sku_field(self, api_client, product_factory: ProductFactory):

        file_data = {
            "name": ["Product 1", "Product 2"],
            "description": ["Description 1", "Description 2"],
            "price": [100.00, 200.00],
            "quantity": [10, 20],
        }
        df = pd.DataFrame(file_data)

        excel_file = BytesIO()
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)

        url = reverse("products:upload")
        response = api_client.post(url, data={"file": excel_file}, format="multipart")

        assert response.status_code == 400

    def test_upload_products_with_invalid_file_extension(self, api_client, product_factory: ProductFactory):

        url = reverse("products:upload")
        txt_file = BytesIO()
        txt_file.write(b"Invalid file")
        txt_file.seek(0)
        response = api_client.post(url, data={"file": txt_file}, format="multipart")

        assert response.status_code == 400