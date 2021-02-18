from django.db import models

class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    discountRate = models.FloatField(max_length=20)
    isActive = models.BooleanField()
    startDate = models.DateTimeField()
    expirationDate = models.DateTimeField()

    class Meta:
        db_table = "Discount"
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return f"{self.name}"
