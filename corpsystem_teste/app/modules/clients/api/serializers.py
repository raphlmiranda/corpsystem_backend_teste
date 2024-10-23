from rest_framework import serializers
from corpsystem_teste.app.modules.clients.models import Client

class BaseSerializer(serializers.ModelSerializer):
    pass


class ClientSerializer(BaseSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'phone', 'address')


class ClientRetrieveSerializer(BaseSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'phone', 'address', 'cpf', 'created_at', 'updated_at')


class ClientCreateSerializer(BaseSerializer):

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'address', 'cpf')


class ClientUpdateSerializer(BaseSerializer):

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'address')
