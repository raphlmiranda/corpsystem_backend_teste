from rest_framework import serializers

from corpsystem_teste.app.modules.sales.models import Sale
from corpsystem_teste.app.modules.sellers.models import Seller
from corpsystem_teste.app.modules.clients.models import Client
from corpsystem_teste.app.modules.products.models import Product



class SaleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('id', 'seller', 'client', 'product', 'quantity', 'price_total', 'status', 'created_at', 'updated_at')


class SaleRetrieveSerializer(SaleListSerializer):
    pass


class SaleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('seller', 'client', 'product', 'quantity', 'price_total')

class SaleUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('status')
