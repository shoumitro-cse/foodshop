from django.db import models

# from . import Users, Invoice
from . import *

class DeliveryAddr(models.Model):
    id = models.AutoField(primary_key=True)
    addr_title = models.CharField(max_length=255)
    p_name = models.CharField(max_length=255)# p_name = person name
    p_phone = models.CharField(max_length=255)
    p_addr1 = models.CharField(max_length=255)
    p_addr2 = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    amount = models.FloatField(max_length=20)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    class Meta:
        db_table = "DeliveryAddr"
        verbose_name = "Delivery Address"
        verbose_name_plural = "Delivery Addresses"
    def __str__(self):
        return f"{self.id}_{self.p_name}"


class OrderInfo(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_at = models.CharField(max_length=225)#date
    shippingSlot = models.CharField(max_length=225)#time
    shippingMethod = models.CharField(max_length=225)#Delivery Type
    note = models.CharField(max_length=225)
    onlinePayment = models.CharField(max_length=225)#Payment Method
    class Meta:
        db_table = "OrderInfo"
        verbose_name = "Order Information"
        verbose_name_plural = "Order Informations"

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=225)# canceled, success
    isPaid = models.CharField(max_length=225)#pending, x, paid
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    deliveryAddr = models.ForeignKey(DeliveryAddr, on_delete=models.CASCADE)
    orderInfo = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    class Meta:
        db_table = "Orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField(max_length=20)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    # invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    class Meta:
        db_table = "Payment"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
