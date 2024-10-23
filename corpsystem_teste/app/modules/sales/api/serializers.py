from rest_framework import serializers

from corpsystem_teste.app.modules.sales.models import Sale
from corpsystem_teste.app.modules.sellers.models import Seller
from corpsystem_teste.app.modules.clients.models import Client
from corpsystem_teste.app.modules.products.models import Product



class SaleListSerializer(serializers.ModelSerializer):

    product = serializers.SlugRelatedField(read_only=True, many=True, slug_field='sku')

    class Meta:
        model = Sale
        fields = ('id', 'seller', 'client', 'product', 'quantity', 'total_price', 'status', 'created_at', 'updated_at')


class SaleRetrieveSerializer(SaleListSerializer):
    pass


class SaleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('seller', 'client', 'product', 'quantity')

class SaleUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('status')
