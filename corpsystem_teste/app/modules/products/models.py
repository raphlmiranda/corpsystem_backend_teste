from django.db import models

from corpsystem_teste.app.mixins.base_models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    image_url = models.URLField()
    quantity = models.IntegerField(default=0, blank=False, null=False)
    sku = models.CharField(max_length=255, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     indexes = ['name', 'sku']
