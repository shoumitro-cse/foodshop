# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    totalitem = models.IntegerField(db_column='totalItem')  # Field name made lowercase.
    totaltaxed = models.FloatField(db_column='totalTaxed')  # Field name made lowercase.
    discount = models.FloatField()
    deliverycost = models.FloatField(db_column='deliveryCost')  # Field name made lowercase.
    totalcost = models.FloatField(db_column='totalCost')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cart'


class Cartitem(models.Model):
    quantity = models.IntegerField()
    totalcost = models.FloatField(db_column='totalCost')  # Field name made lowercase.
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CartItem'


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Category'


class Deliveryaddr(models.Model):
    addr_title = models.CharField(max_length=255)
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=255)
    p_addr1 = models.CharField(max_length=255)
    p_addr2 = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    amount = models.FloatField()
    invoice = models.ForeignKey('Invoice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DeliveryAddr'


class Discount(models.Model):
    name = models.CharField(max_length=255)
    discountrate = models.FloatField(db_column='discountRate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='expirationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Discount'


class Invoice(models.Model):
    totalitem = models.IntegerField(db_column='totalItem')  # Field name made lowercase.
    totaltaxed = models.FloatField(db_column='totalTaxed')  # Field name made lowercase.
    discount = models.FloatField()
    deliverycost = models.FloatField(db_column='deliveryCost')  # Field name made lowercase.
    totalcost = models.FloatField(db_column='totalCost')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invoice'


class Invoiceitem(models.Model):
    quantity = models.IntegerField()
    totalcost = models.FloatField(db_column='totalCost')  # Field name made lowercase.
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'InvoiceItem'


class Login(models.Model):
    user_name = models.CharField(unique=True, max_length=255)
    u_password = models.CharField(max_length=100)
    u_re_password = models.CharField(max_length=100)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Login'


class Orderinfo(models.Model):
    submitted_at = models.CharField(max_length=225)
    shippingslot = models.CharField(db_column='shippingSlot', max_length=225)  # Field name made lowercase.
    shippingmethod = models.CharField(db_column='shippingMethod', max_length=225)  # Field name made lowercase.
    note = models.CharField(max_length=225)
    onlinepayment = models.CharField(db_column='onlinePayment', max_length=225)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderInfo'


class Orders(models.Model):
    status = models.CharField(max_length=225)
    ispaid = models.CharField(db_column='isPaid', max_length=225)  # Field name made lowercase.
    deliveryaddr = models.ForeignKey(Deliveryaddr, models.DO_NOTHING, db_column='deliveryAddr_id')  # Field name made lowercase.
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    orderinfo = models.ForeignKey(Orderinfo, models.DO_NOTHING, db_column='orderInfo_id')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Orders'


class Payment(models.Model):
    amount = models.FloatField()
    order = models.ForeignKey(Orders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Payment'


class Product(models.Model):
    name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=5000)
    weight = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    stock = models.IntegerField()
    currentstock = models.IntegerField(db_column='currentStock')  # Field name made lowercase.
    price = models.FloatField()
    unitprice = models.FloatField(db_column='unitPrice')  # Field name made lowercase.
    taxed = models.FloatField()
    discount = models.ForeignKey(Discount, models.DO_NOTHING)
    productcategory = models.ForeignKey('Productcategory', models.DO_NOTHING, db_column='productCategory_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Productcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProductCategory'


class Productinfo(models.Model):
    desc1 = models.CharField(max_length=255)
    desc2 = models.CharField(max_length=255)
    desc3 = models.CharField(max_length=255)
    desc4 = models.CharField(max_length=255)
    image1 = models.CharField(max_length=100)
    image2 = models.CharField(max_length=100)
    image3 = models.CharField(max_length=100)
    image4 = models.CharField(max_length=100)
    product = models.OneToOneField(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProductInfo'


class Users(models.Model):
    fullname = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.CharField(unique=True, max_length=255)
    gender = models.CharField(max_length=1)
    postcode = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
