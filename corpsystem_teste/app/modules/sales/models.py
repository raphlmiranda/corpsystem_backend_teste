from django.db import models

from corpsystem_teste.app.mixins.base_models import BaseModel

ENUM_SALE_STATUS = (
    ('PENDING', 'Pendente'),
    ('APPROVED', 'Aprovado'),
    ('REJECTED', 'Rejeitado'),
)

class Sale(BaseModel):

    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, blank=False, null=False)
    seller = models.ForeignKey("sellers.Seller", on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    status = models.CharField(max_length=10, choices=ENUM_SALE_STATUS, default='PENDING')
