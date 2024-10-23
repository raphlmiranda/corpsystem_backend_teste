from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response

import pandas as pd

from corpsystem_teste.app.modules.products.models import Product


class ProductsImportActions:

    def __validate_excel_file(self, file) -> bool:
        list_necessary_rows = ["name", "description", "price", "sku", "quantity"]
        df = pd.read_excel(file)
        for row in list_necessary_rows:
            if row not in df.columns:
                return False
        return True
    
    def __validate_file_extension(self, file) -> bool:
        return file.name.endswith('.xlsx')

    @action(methods=['POST'], detail=False)
    def import_product_file(self, request, *args, **kwargs):
        object_file = request.FILES['file']

        if not self.__validate_file_extension(object_file):
            return Response({"message": "Extensão do arquivo inválida"}, status=400)

        df = pd.read_excel(object_file)
        validated_file = self.__validate_excel_file(object_file)
        if not validated_file:
            return Response({"message": "Arquivo inválido"}, status=400)
        for index, row in df.iterrows():
            Product.objects.create(
                name=row['name'],
                description=row['description'],
                price=row['price'],
                sku=row['sku'],
                quantity=row['quantity'],
                is_active=True
            )
        return Response(
            {
                "message": "Produtos importados com sucesso"
            },
            status=201
        )
            

