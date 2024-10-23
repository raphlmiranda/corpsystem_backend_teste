from corpsystem_teste.app.modules.products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image_url', 'quantity', 'sku', 'is_active')


class ProductListActivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image_url', 'quantity', 'sku', 'is_active')


class ProductRetrieveSerializer(ProductSerializer):
    pass


class ProductCreateSerializer(serializers.ModelSerializer):
    
    image_url = serializers.URLField(required=False)
    sku = serializers.CharField(required=True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image_url', 'quantity', 'sku')


class ProductUpdateSerializer(ProductSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image_url', 'quantity', 'sku', 'is_active')

    def update(self, instance, validated_data):
        invalidated_keys = ['sku']
        if any(key in invalidated_keys for key in validated_data):
            raise serializers.ValidationError('Não é possível alterar o SKU ou o status do produto')
        return super().update(instance, validated_data)

