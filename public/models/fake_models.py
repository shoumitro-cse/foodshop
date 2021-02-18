# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.db import models
#
# # Create your models here.
# #From Django docs, Options.managed:
# # "If False, no database table creation or deletion operations will be performed for this model."
# # from django.forms import forms
# from django import forms
#
# # operations = [
# #     migrations.RunSQL("ALTER TABLE Users AUTO_INCREMENT=1000000;"),
# #     migrations.RunSQL("ALTER TABLE Login AUTO_INCREMENT=2000000;"),
# #     migrations.RunSQL("ALTER TABLE Category AUTO_INCREMENT=3000000;"),
# #     migrations.RunSQL("ALTER TABLE ProductCategory AUTO_INCREMENT=1700000;"),
# #     migrations.RunSQL("ALTER TABLE Discount AUTO_INCREMENT=5000000;"),
# #     migrations.RunSQL("ALTER TABLE Product AUTO_INCREMENT=6000000;"),
# #     migrations.RunSQL("ALTER TABLE ProductInfo AUTO_INCREMENT=7000000;"),
# #     migrations.RunSQL("ALTER TABLE Cart AUTO_INCREMENT=8000000;"),
# #     migrations.RunSQL("ALTER TABLE CartItem AUTO_INCREMENT=9000000;"),
# #     migrations.RunSQL("ALTER TABLE Invoice AUTO_INCREMENT=1100000;"),
# #     migrations.RunSQL("ALTER TABLE InvoiceItem AUTO_INCREMENT=1200000;"),
# #     migrations.RunSQL("ALTER TABLE DeliveryAddr AUTO_INCREMENT=1300000;"),
# #     migrations.RunSQL("ALTER TABLE OrderInfo AUTO_INCREMENT=1400000;"),
# #     migrations.RunSQL("ALTER TABLE Orders AUTO_INCREMENT=1500000;"),
# #     migrations.RunSQL("ALTER TABLE Payment AUTO_INCREMENT=1600000;"),
# # ]
#
# # ALTER TABLE Users AUTO_INCREMENT=1000000;
# # ALTER TABLE Login AUTO_INCREMENT=2000000;
# # ALTER TABLE Category AUTO_INCREMENT=3000000;
# # ALTER TABLE ProductCategory AUTO_INCREMENT=1700000;
# # ALTER TABLE Discount AUTO_INCREMENT=5000000;
# # ALTER TABLE Product AUTO_INCREMENT=6000000;
# # ALTER TABLE ProductInfo AUTO_INCREMENT=7000000;
# # ALTER TABLE Cart AUTO_INCREMENT=8000000;
# # ALTER TABLE CartItem AUTO_INCREMENT=9000000;
# # ALTER TABLE Invoice AUTO_INCREMENT=1100000;
# # ALTER TABLE InvoiceItem AUTO_INCREMENT=1200000;
# # ALTER TABLE DeliveryAddr AUTO_INCREMENT=1300000;
# # ALTER TABLE OrderInfo AUTO_INCREMENT=1400000;
# # ALTER TABLE Orders AUTO_INCREMENT=1500000;
# # ALTER TABLE Payment AUTO_INCREMENT=1600000;
#
# # DROP TABLE Payment;
# # DROP TABLE Orders;
# # DROP TABLE OrderInfo;
# # DROP TABLE DeliveryAddr;
# # DROP TABLE InvoiceItem;
# # DROP TABLE Invoice;
# # DROP TABLE CartItem;
# # DROP TABLE Cart;
# # DROP TABLE ProductInfo;
# # DROP TABLE Product;
# # DROP TABLE Discount ;
# # DROP TABLE ProductCategory;
# # DROP TABLE Category;
# # DROP TABLE Login;
# # DROP TABLE Users;
# from django.urls import reverse
#
# from django.utils.html import format_html
# from django_cleanup import cleanup
#
#
# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#
#     class Meta:
#         db_table = "Category"
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"
#
#     def __str__(self):
#         return f"{self.name}"
#
# class ProductCategory(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = "ProductCategory"
#         verbose_name = "ProductCategory"
#         verbose_name_plural = "ProductCategories"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Discount(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     discountRate = models.FloatField(max_length=20)
#     isActive = models.BooleanField()
#     startDate = models.DateTimeField()
#     expirationDate = models.DateTimeField()
#
#     class Meta:
#         db_table = "Discount"
#         verbose_name = "Discount"
#         verbose_name_plural = "Discounts"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Product(models.Model):
#     BRAND_1 = 'Brand'
#     BRAND_2 = 'No Brand'
#
#     BRAND_CHOICES = (
#         (BRAND_1, 'Brand'),
#         (BRAND_2, 'NO Brand'),
#     )
#     brand_name = (
#         ('S', 'brand'),
#         ('M', 'no brand'),
#         ('L', 'company'),
#     )
#     id = models.AutoField(primary_key=True)
#     productCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#     discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     keyword = models.CharField(max_length=5000)
#     weight = models.CharField(max_length=255)
#     brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
#     stock = models.IntegerField()
#     currentStock = models.IntegerField()
#     price = models.FloatField(max_length=20)
#     unitPrice = models.FloatField(max_length=20)
#     taxed = models.FloatField(max_length=20, default=0.0)
#     class Meta:
#         db_table = "Product"
#        # proxy = True#A proxy model extends the functionality of another model without creating an actual table in the database.
#         # managed = True
#         verbose_name = "Product"
#         verbose_name_plural = "Products"
#         ordering = ("id", "name")
#
#     def __str__(self):
#         return f"{self.id}_{self.name}" # return f"{self.name}, {self.price}"
#
# # #this commend ignore cleanup
# # @cleanup.ignore
# class ProductInfo(models.Model):
#     id = models.AutoField(primary_key=True)
#     # product = models.ManyToManyField(Product)#Many-to-Many fields:
#     # product = models.ForeignKey(Product, on_delete=models.CASCADE)#Many-to-one fields:
#     product = models.OneToOneField(Product, on_delete=models.CASCADE)#One-to-one fields:
#     desc1 = models.CharField(max_length=255)
#     desc2 = models.CharField(max_length=255)
#     desc3 = models.CharField(max_length=255)
#     desc4 = models.CharField(max_length=255)
#     #img uploaded to /media/product directory
#     image1 = models.ImageField(upload_to='product')
#     image2 = models.ImageField(upload_to='product')
#     image3 = models.ImageField(upload_to='product')
#     image4 = models.ImageField(upload_to='product')
#     # image1.__str__()
#     # image1.name
#     class Meta:
#         db_table = "ProductInfo"
#         verbose_name = "Product Information"
#         verbose_name_plural = "Product Informations"
#
#     def __str__(self):
#         return f"{self.id}"
#
#
# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
#     totalItem = models.IntegerField(default=0)
#     totalTaxed = models.FloatField(max_length=20, default=0.0)
#     discount = models.FloatField(max_length=20, default=0.0)
#     deliveryCost = models.FloatField(max_length=20, default=0.0)
#     totalCost = models.FloatField(max_length=20, default=0.0)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
#     class Meta:
#         db_table = "Cart"
#         verbose_name = "Cart"
#         verbose_name_plural = "Carts"
#
# class CartItem(models.Model):
#     id = models.AutoField(primary_key=True)
#     quantity = models.IntegerField()
#     totalCost = models.FloatField(max_length=20)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     class Meta:
#         db_table = "CartItem"
#         verbose_name = "Cart Item"
#         verbose_name_plural = "Cart Items"
#
#
# class Invoice(models.Model):
#     id = models.AutoField(primary_key=True)
#     totalItem = models.IntegerField(default=0)
#     totalTaxed = models.FloatField(max_length=20, default=0.0)
#     discount = models.FloatField(max_length=20, default=0.0)
#     deliveryCost = models.FloatField(max_length=20, default=0.0)
#     totalCost = models.FloatField(max_length=20, default=0.0)
#     class Meta:
#         db_table = "Invoice"
#         verbose_name = "Invoice"
#         verbose_name_plural = "Invoices"
#
# class InvoiceItem(models.Model):
#     id = models.AutoField(primary_key=True)
#     quantity = models.IntegerField()
#     totalCost = models.FloatField(max_length=20)
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     class Meta:
#         db_table = "InvoiceItem"
#         verbose_name = "Invoice Item"
#         verbose_name_plural = "Invoice Items"
# class DeliveryAddr(models.Model):
#     id = models.AutoField(primary_key=True)
#     addr_title = models.CharField(max_length=255)
#     p_name = models.CharField(max_length=255)# p_name = person name
#     p_phone = models.CharField(max_length=255)
#     p_addr1 = models.CharField(max_length=255)
#     p_addr2 = models.CharField(max_length=255)
#     area = models.CharField(max_length=255)
#     zip = models.CharField(max_length=255)
#     amount = models.FloatField(max_length=20)
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     class Meta:
#         db_table = "DeliveryAddr"
#         verbose_name = "Delivery Address"
#         verbose_name_plural = "Delivery Addresses"
#     def __str__(self):
#         return f"{self.id}_{self.p_name}"
#
#
# class OrderInfo(models.Model):
#     id = models.AutoField(primary_key=True)
#     submitted_at = models.CharField(max_length=225)#date
#     shippingSlot = models.CharField(max_length=225)#time
#     shippingMethod = models.CharField(max_length=225)#Delivery Type
#     note = models.CharField(max_length=225)
#     onlinePayment = models.CharField(max_length=225)#Payment Method
#     class Meta:
#         db_table = "OrderInfo"
#         verbose_name = "Order Information"
#         verbose_name_plural = "Order Informations"
#
# class Orders(models.Model):
#     id = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=225)# canceled, success
#     isPaid = models.CharField(max_length=225)#pending, x, paid
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     deliveryAddr = models.ForeignKey(DeliveryAddr, on_delete=models.CASCADE)
#     orderInfo = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
#     class Meta:
#         db_table = "Orders"
#         verbose_name = "Order"
#         verbose_name_plural = "Orders"
#
# class Payment(models.Model):
#     id = models.AutoField(primary_key=True)
#     amount = models.FloatField(max_length=20)
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE)
#     # invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     class Meta:
#         db_table = "Payment"
#         verbose_name = "Payment"
#         verbose_name_plural = "Payments"
#
