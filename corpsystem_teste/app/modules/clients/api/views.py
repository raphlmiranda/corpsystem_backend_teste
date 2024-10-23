from typing import List
from validate_docbr import CPF
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from corpsystem_teste.app.mixins.viewsets import BaseView
from corpsystem_teste.app.modules.clients.models import Client
from .serializers import (
    ClientSerializer,
    ClientRetrieveSerializer,
    ClientCreateSerializer,
    ClientUpdateSerializer
)


class ClientsViewSet(BaseView):

    serializers = {
        'list': ClientSerializer,
        'retrieve': ClientRetrieveSerializer,
        'create': ClientCreateSerializer,
        'partial_update': ClientUpdateSerializer,
        'update': ClientUpdateSerializer
    }

    permission_classes = [AllowAny]

    def get_queryset(self) -> List[Client]:
        return Client.objects.all()
    
    def create(self, request, *args, **kwargs):
        cpf = CPF()
        if not cpf.validate(request.data['cpf']):
            return Response({'cpf': 'CPF inválido'}, status=400)
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        if 'cpf' in request.data:
            return Response({'cpf': 'CPF não pode ser alterado'}, status=400)
        return super().partial_update(request, *args, **kwargs)
         
