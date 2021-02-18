from django.db import models

# from . import Users, Product
from . import *


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    totalItem = models.IntegerField(default=0)
    totalTaxed = models.FloatField(max_length=20, default=0.0)
    discount = models.FloatField(max_length=20, default=0.0)
    deliveryCost = models.FloatField(max_length=20, default=0.0)
    totalCost = models.FloatField(max_length=20, default=0.0)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = "Cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    totalCost = models.FloatField(max_length=20)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    class Meta:
        db_table = "CartItem"
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
