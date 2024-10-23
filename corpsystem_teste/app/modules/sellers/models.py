from django.db import models

from corpsystem_teste.app.mixins.base_models import BaseModel


class Seller(BaseModel):
    
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name