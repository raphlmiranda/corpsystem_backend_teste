from corpsystem_teste.app.mixins.base_models import BaseModel
from django.db import models

from validate_docbr import CPF


class Client(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
    
    def clean(self):
        cpf = CPF()
        if self.cpf is None or self.cpf == '':
            return
        if not cpf.validate(self.cpf):
            raise ValidationError({
                'cpf': 'CPF inválido'
            })
    
    class Meta:
        indexes = [
            models.Index(fields=['cpf', 'email'], name='client_unique_cpf_email_idx'),
        ]