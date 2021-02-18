from django.db import models

# from . import Users, Product
from . import *

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    totalItem = models.IntegerField(default=0)
    totalTaxed = models.FloatField(max_length=20, default=0.0)
    discount = models.FloatField(max_length=20, default=0.0)
    deliveryCost = models.FloatField(max_length=20, default=0.0)
    totalCost = models.FloatField(max_length=20, default=0.0)
    class Meta:
        db_table = "Invoice"
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    totalCost = models.FloatField(max_length=20)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    class Meta:
        db_table = "InvoiceItem"
        verbose_name = "Invoice Item"
        verbose_name_plural = "Invoice Items"