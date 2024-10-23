from typing import List
from django.http.request import QueryDict
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from corpsystem_teste.app.mixins.viewsets import BaseView
from corpsystem_teste.app.modules.products.models import Product
from .serializers import (
    ProductSerializer,
    ProductRetrieveSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer
)


class ProductsViewSet(BaseView):

    serializers = {
        'default': ProductSerializer,
        'retrieve': ProductRetrieveSerializer,
        'create': ProductCreateSerializer,
        'partial_update': ProductUpdateSerializer,
    }
    permission_classes = [AllowAny]
    filterset_fields = ['sku', 'name', 'is_active']
    
    def get_queryset(self) -> List[Product]:
        return Product.objects.all()
    
    def create(self, request, *args, **kwargs):
        quantity = int(request.data.get('quantity'))
        if quantity < 1:
            return Response(
                {'quantity': "Quantidade do Produto deve ser maior que 0"},
                status=400
            )
        product = Product.objects.filter(sku=request.data.get('sku'))
        if product:
            return Response(
                {'sku': "Produto já existe"},
                status=400
            )
        print(type(request.data))
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data['is_active'] = True
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        quantity = int(request.data.get('quantity'))
        if quantity < 1:
            request.data._mutable = True
            request.data['is_active'] = False
            request.data._mutable = False
        return super().partial_update(request, *args, **kwargs)
