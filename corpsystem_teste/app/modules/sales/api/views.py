from typing import Any, List
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from corpsystem_teste.app.mixins.viewsets import BaseView
from corpsystem_teste.app.modules.sales.models import Sale
from corpsystem_teste.app.modules.sellers.models import Seller
from corpsystem_teste.app.modules.clients.models import Client
from corpsystem_teste.app.modules.products.models import Product

from .serializers import (
    SaleListSerializer,
    SaleRetrieveSerializer,
    SaleCreateSerializer
)
from corpsystem_teste.app.modules.sales.utils.export import SalesExportUtils


class SaleExportView(APIView):

    def get(self, request, *args, **kwargs) -> HttpResponse:
        export_utils = SalesExportUtils()
        return export_utils.export(request)


class SalesViewSet(BaseView):

    serializers = {
        'default': SaleListSerializer,
        'retrieve': SaleRetrieveSerializer,
        'create': SaleCreateSerializer
    }
    permission_classes = [AllowAny]
    filterset_fields = ["created_at", "seller", "client"]

    def get_queryset(self) -> List[Sale]:
        return Sale.objects.all()

    def validate(self, data: dict) -> dict:
        seller = Seller.objects.filter(pk=data.get('seller'))
        client = Client.objects.filter(pk=data.get('client'))
        product = Product.objects.filter(pk=data.get('product'))

        if not seller:
            return {'message': 'Vendedor não encontrado'}
        if not client:
            return {'message': 'Cliente não encontrado'}
        if not product:
            return {'message': 'Produto não encontrado'}

        return data
    
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            data = self.validate(request.data)
            if data.get('message'):
                return Response(data, status=400)
            product = Product.objects.get(pk=data.get('product'))
            if product.quantity < request.data.get('quantity'):
                return Response({'message': 'Quantidade maior que o estoque'}, status=400)
            product.quantity -= request.data.get('quantity')
            product.save()

            validate_data = request.data.copy()
            validate_data['price_total'] = product.price * request.data.get('quantity')
            serializer = self.get_serializer(data=validate_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'message': 'Produto não encontrado'}, status=400)