from django.db import models
from django_cleanup import cleanup

# from . import *
from .category_model import ProductCategory
from .discount_model import Discount

from django.db import connection

class ProductManager(models.Manager):
    pass
    # def create_product(self, name):
    #     product = self.create(name=name)
    #     # do something with the product
    #     return product

    # def get_queryset(self):
    #     return super().get_queryset().filter(author='Roald Dahl')

    #custom sql
    def my_custom_sql(self):

        # c = connection.cursor()
        # try:
        #     c.execute("select * from Product")
        # finally:
        #     c.close()

        #as same
        with connection.cursor() as cursor:
            # cursor.execute("other product sql cmd")
            cursor.execute("select * from Product")
            # row = cursor.fetchone() # one row fetch
            row = cursor.fetchall() #all result
        return row

    def productFilter(self):
        return self.filter(role='A')

    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""select * from Product""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], name=row[1], keyword=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list

    @classmethod #class method
    def other_fun(self):
        pass

# Manager class inherit QuerySet class
# class Manager(BaseManager.from_queryset(QuerySet)):
#     pass

class Product(models.Model):
    BRAND_1 = 'Brand'
    BRAND_2 = 'No Brand'

    objects = ProductManager() #custom Manager objects

    # objects = models.Manager()  # The default manager.

    #this is a invisiable attribute
    # objects = django.db.models.manager.Manager()
    # type(Product.objects) #<class 'django.db.models.manager.Manager'>

    #class attribute
    BRAND_CHOICES = (
        (BRAND_1, 'Brand'),
        (BRAND_2, 'NO Brand'),
    )
    brand_name = (
        ('S', 'brand'),
        ('M', 'no brand'),
        ('L', 'company'),
    )
    id = models.AutoField(primary_key=True)
    productCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="product_set")
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=5000)
    weight = models.CharField(max_length=255)
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    stock = models.IntegerField()
    currentStock = models.IntegerField()
    price = models.FloatField(max_length=20)
    unitPrice = models.FloatField(max_length=20)
    taxed = models.FloatField(max_length=20, default=0.0)
    class Meta:
        db_table = "Product"
       # proxy = True#A proxy model extends the functionality of another model without creating an actual table in the database.
        # managed = True
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("id", "name")

    def __str__(self):
        return f"{self.id}_{self.name}" # return f"{self.name}, {self.price}"

# #this commend ignore cleanup
# @cleanup.ignore
class ProductInfo(models.Model):
    id = models.AutoField(primary_key=True)
    # product = models.ManyToManyField(Product)#Many-to-Many fields:
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)#Many-to-one fields:
    product = models.OneToOneField(Product, on_delete=models.CASCADE)#One-to-one fields:
    desc1 = models.CharField(max_length=255)
    desc2 = models.CharField(max_length=255)
    desc3 = models.CharField(max_length=255)
    desc4 = models.CharField(max_length=255)
    #img uploaded to /media/product directory
    image1 = models.ImageField(upload_to='product')
    image2 = models.ImageField(upload_to='product')
    image3 = models.ImageField(upload_to='product')
    image4 = models.ImageField(upload_to='product')
    # image1.__str__()
    # image1.name
    class Meta:
        db_table = "ProductInfo"
        verbose_name = "Product Information"
        verbose_name_plural = "Product Informations"
        ordering = ("-id", )

    def __str__(self):
        return f"{self.id}"
