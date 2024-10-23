from rest_framework import serializers

from corpsystem_teste.app.modules.sellers.models import Seller


class SellerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name', 'email')


class SellerRetrieveSerializer(SellerListSerializer):
    pass


class SellerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('name', 'email')


class SellerUpdateSerializer(SellerListSerializer):
    class Meta:
        model = Seller
        fields = ('name', 'email')
