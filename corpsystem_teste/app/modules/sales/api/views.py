from typing import Any, List
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from corpsystem_teste.app.mixins.viewsets import BaseView
from corpsystem_teste.app.modules.sales.models import Sale
from corpsystem_teste.app.modules.products.models import Product

from .serializers import (
    SaleListSerializer,
    SaleRetrieveSerializer,
    SaleCreateSerializer
)
from .actions import SalesActions


class SalesViewSet(SalesActions, BaseView):

    serializers = {
        'default': SaleListSerializer,
        'retrieve': SaleRetrieveSerializer,
        'create': SaleCreateSerializer,
        'export': SaleListSerializer
    }
    permission_classes = [AllowAny]

    def get_queryset(self) -> List[Sale]:
        return Sale.objects.all()
    
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        product = Product.objects.get(pk=request.data.get('product'))
        if product.quantity < request.data.get('quantity'):
            return Response({'message': 'Quantidade maior que o estoque'}, status=400)
        product.quantity -= request.data.get('quantity')
        product.save()
        request.data._mutable = True
        request.data['total_price'] = product.price * request.data.get('quantity')
        request.data._mutable = False
        return super().create(request, *args, **kwargs)