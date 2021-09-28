import uuid

from django.db import models
from django.utils import timezone


class Product(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name
