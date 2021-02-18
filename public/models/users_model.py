from django.db import models

class Users(models.Model):

    class GENDER(models.TextChoices):
        GENDER_FEMALE = 'F', ('Female')
        GENDER_MALE = 'M', ('Male')

    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'

    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )
    id = models.AutoField(primary_key=True)

    fullname = models.CharField(help_text="Please input full name.", max_length=250)

    fullname.error_messages = "Custom Fullname error msg from model"
    fullname.default_error_messages = "default fullname error from model"
    fullname.name = "fullname"
    fullname.verbose_name = "Full Name" # Field label name
    fullname.db_column = "fullname"
    # fullname.description = ("String (up to %(max_length)s)")
    # fullname.attname = "fullname"
    # fullname.to_python()
    # fullname.get_internal_type()
    # fullname.db_type()
    # fullname.deconstruct()

    # fullname.empty_strings_allowed = True
    # fullname.empty_values =
    # fullname.creation_counter = 0
    # fullname.auto_creation_counter = -1
    # fullname.default_validators = []  # Default set of validators
    # fullname.default_error_messages = {
    #     'invalid_choice': ('Value  is not a valid choice.'),
    #     'null': ('This field cannot be null.'),
    #     'blank': ('This field cannot be blank.'),
    #     'unique': ('field label already exists.'),
    #     'unique_for_date': ("field must be unique for "),
    # }
    #
    #
    # fullname.system_check_deprecated_details = None
    # fullname.system_check_removed_details = None
    #
    # fullname.hidden = False

    # Field Relation Attribute

    # fullname.many_to_many = None
    # fullname.many_to_one = None
    # fullname.one_to_many = None
    # fullname.one_to_one = None
    # fullname.related_model = None

    # other Field Attribute

    # fullname.name =
    # fullname.verbose_name =
    # fullname._verbose_name =
    # fullname.primary_key =
    # fullname.max_length =
    # fullname._unique =
    # fullname.blank =
    # fullname.null =
    # fullname.remote_field =
    # fullname.is_relation =
    # fullname.default =
    # fullname.editable =
    # fullname.serialize =
    # fullname.unique_for_date =
    # fullname.unique_for_month =
    # fullname.unique_for_year =
    # fullname.choices =
    # fullname.help_text =
    # fullname.db_index =
    # fullname.db_column =
    # fullname._db_tablespace =
    # fullname.auto_created =
    # fullname._error_messages =
    # fullname.creation_counter =

    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) #same
    # gender = models.CharField(max_length=1, choices=GENDER.choices) #same
    postcode = models.CharField(max_length=250)

    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("email",)
        # default_permissions = ()
        # permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]
        # indexes = [
        #     models.Index(fields=['last_name', 'first_name']),
        #     models.Index(fields=['first_name'], name='first_name_idx'),
        # ]

       # from path/to/django/db/models/ options.py
        # _get_fields_cache = {}
        # local_fields = []
        # local_many_to_many = []
        # private_fields = []
        # local_managers = []
        # base_manager_name = None
        # default_manager_name = None
        # model_name = None
        # verbose_name = None
        # verbose_name_plural = None
        # db_table = ''
        # ordering = []
        # _ordering_clash = False
        # indexes = []
        # constraints = []
        # unique_together = []
        # index_together = []
        # select_on_save = False
        # default_permissions = ('add', 'change', 'delete', 'view')
        # permissions = []
        # object_name = None
        # app_label = app_label
        # get_latest_by = None
        # order_with_respect_to = None
        # db_tablespace = settings.DEFAULT_TABLESPACE
        # required_db_features = []
        # required_db_vendor = None
        # meta = meta
        # pk = None
        # auto_field = None
        # abstract = False
        # managed = True
        # proxy = False
        # proxy_for_model = None
        # concrete_model = None
        # swappable = None
        # parents = {}
        # auto_created = False
        #
        # related_fkey_lookups = []
        # apps =
        # default_related_name = None

    # def get_absolute_url(self):
    #     return reverse('user-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.fullname}"





# max_length=255
# primary_key=True
# unique=True # unique db attribure
# default=100000 #for set default db atrribute value


# owner = models.ForeignKey("User", on_delete=models.CASCADE)
class Login(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, unique=True)
    u_password = models.CharField(max_length=100)
    u_re_password = models.CharField(max_length=100)

    class Meta:
        db_table = "Login"
        verbose_name = "Login"
        verbose_name_plural = "Logins"

    def __str__(self):
        return f"{self.user_name}"