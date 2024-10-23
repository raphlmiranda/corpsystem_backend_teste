from factory.django import DjangoModelFactory

from corpsystem_teste.app.modules.clients.models import Client


class ClientFactory(DjangoModelFactory):

    name = 'Client Test'
    email = 'client@test.com'
    phone = '99999999999'
    cpf = '99999999999'
    address = 'Address Test'

    class Meta:
        model = Client
        django_get_or_create = ["email"]
        skip_postgeneration_save = True