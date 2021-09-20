import uuid

from django.db import models
from django.utils import timezone


class Product(models.Model):

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(
        null=True, blank=True, default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


# class CartItem(models.Model):

#     id = models.AutoField(primary_key=True)
#     quantity = models.IntegerField(null=True, blank=True)
#     product = models.ForeignKey(
#         'Product', on_delete=models.CASCADE, related_name='cartitems')
#     # user = models.ForeignKey(
#         # 'User', on_delete=models.CASCADE, related_name='cartitems')

#     class Meta:
#         db_table = "cartItem"
    
#     def __str__(self):
#         return self.product.name
