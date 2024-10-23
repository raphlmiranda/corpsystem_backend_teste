from typing import List
from rest_framework.permissions import AllowAny

from corpsystem_teste.app.mixins.viewsets import BaseView
from corpsystem_teste.app.modules.sellers.models import Seller
from .serializers import (
    SellerListSerializer,
    SellerRetrieveSerializer,
    SellerCreateSerializer,
    SellerUpdateSerializer
)


class SellersViewSet(BaseView):

    serializers = {
        'default': SellerListSerializer,
        'retrieve': SellerRetrieveSerializer,
        'create': SellerCreateSerializer,
        'partial_update': SellerUpdateSerializer,
    }
    permission_classes = [AllowAny]

    def get_queryset(self) -> List[Seller]:
        return Seller.objects.all()