from django.contrib import admin, messages

# Register your models here.
from django import forms
from django.db.models import Count, Sum
from django.forms import Textarea, TextInput, URLInput, SelectMultiple, Select
from django.shortcuts import render
from django.urls import reverse, path
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import ngettext

# from public.models import Users, Login, Category,ProductCategory, Discount, ProductInfo, Product, Cart, CartItem, Invoice, InvoiceItem, DeliveryAddr, OrderInfo, Orders, Payment
from public.models import *

admin.site.empty_value_display = 'This Field Empty Value'
# admin.site.disable_action('delete_selected') #remove delete action

#simple model table add example
# admin.site.register(Category)



@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("fullname", "address","email","gender")
    pass

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "u_password","u_re_password",)
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "categoryAction")
    empty_value_display = 'No Value'
    search_fields = ("name", )
    list_display_links = None

    def categoryAction(self, obj):
        edit_url = reverse('admin:public_category_change', args=(obj.id,))
        delete_url = reverse('admin:public_category_delete', args=(obj.id,))
        history_url = reverse('admin:public_category_history', args=(obj.id,))
        return format_html("<a class='rec_edit' href='{}' ><b><i>edit</i></b></a> "
                           "\ <a class='rec_delete' href='{}' ><b><i>delete</i></b></a>"
                           "\ <a class='rec_history' href='{}' ><b><i>history</i></b></a>"
                           , edit_url, delete_url, history_url)
    categoryAction.short_description = "Action"

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "productCategoryAction")
    empty_value_display = 'No Value'
    search_fields = ("name", )
    list_per_page = 10
    list_display_links = None

    def productCategoryAction(self, obj):
        edit_url = reverse('admin:public_productcategory_change', args=(obj.id,))
        delete_url = reverse('admin:public_productcategory_delete', args=(obj.id,))
        history_url = reverse('admin:public_productcategory_history', args=(obj.id,))
        return format_html("<a class='rec_edit' href='{}' ><b><i>edit</i></b></a> "
                           "\ <a class='rec_delete' href='{}' ><b><i>delete</i></b></a>"
                           "\ <a class='rec_history' href='{}' ><b><i>history</i></b></a>"
                           , edit_url, delete_url, history_url)
    productCategoryAction.short_description = "Action"

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "discountRate", "isActive", "startDate", "expirationDate")
    empty_value_display = 'No Value'
    search_fields = ("name", )


# class CartItemAdmin(admin.StackedInline):
#     model = CartItem

class ProductInfoTableAdmin(admin.StackedInline): #for parameter => admin.TabularInline, admin.ModelAdmin
    model = ProductInfo

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ('name', 'keyword', )
        fields = "__all__"
        # exclude = ['keyword']
        labels = {
            'name': ('Name Writer'),
        }
        help_texts = {
            'name': ('<b style="color: green">Some useful help text.</b>'),
            'keyword': ('<b style="color: green">Some useful help text.</b>'),
        }
        error_messages = {
            'name': {
                'max_length': ("Some Error Message"),
            },
            'keyword': {
                'max_length': ("Some Error Message"),
            },
        }
        widgets = {
            'keyword': Textarea(attrs={'cols': 40, 'rows': 2}),
            'name': TextInput(attrs={'size': 35}),
        }


    def clean_name(self):
        if self.cleaned_data["name"] == "shoumitro":
            raise forms.ValidationError("Invalid Name field")
        return self.cleaned_data["name"]

# class FilterWithCustomTemplate(admin.SimpleListFilter):
#     template = "cart.html"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #inlines = [ProductInfoAdmin, CartItemAdmin]
    inlines = [ProductInfoTableAdmin] # join product and child table ProductInfo
    list_display = ("id", "name", "weight", "brand", "productCategory", "discount", "stock", "currentStock",
                    "price", "productAction")
    # list_display_links = ("name", ) # make name column link like <a href=''> tomato </a>
    list_display_links = None

    empty_value_display = 'No Value'
    search_fields = ("name", "weight", )

    # customize => search_fields
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            # search_term_as_int = int(search_term)
            search_term_as_int = search_term
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(name=search_term_as_int)
        return queryset, use_distinct

    list_select_related = ('productCategory','discount')

    # list_filter = ("name", )
#    list_filter = (
#        ('name', admin.AllValuesFieldListFilter),
#    )

    form = ProductAdminForm
    # readonly_fields = ("name", )
    list_editable = ("stock", "currentStock", )

    list_per_page = 20
    # list_max_show_all = 200 #Set list_max_show_all to control how many items can appear on a “Show all” admin change list page
    # paginator = 1

    prepopulated_fields = {"keyword": ("name","weight",)}
    preserve_filters = False
    # radio_fields = {"productCategory": admin.VERTICAL}
    ordering = ['id']
    autocomplete_fields = ['productCategory','discount']
    # raw_id_fields = ("productCategory",) # not include add (+)

    save_as = True #By default, save_as is set to False.
    save_as_continue = False #By default, save_as_continue is set to True.
    save_on_top = True #By default, save_on_top is set to False.

    # view_on_site = False
    change_form_template = 'admin/change_form.html' #Change Add Form
    # change_form_template = 'tutorial.html' #Change Edit Form
    # add_form_template = 'tutorial.html' #Change Add Form
    # view_on_site = 'tutorial.html' #Change site
    # change_list_template = "tutorial.html" # for View or List Table
    # delete_confirmation_template = "tutorial.html" #delete confirmation template
    # delete_selected_confirmation_template = "fale.html"
    # object_history_template = "tutorial.html" #history template
    # popup_response_template = "tutorial.html"


    # for custom action
    def make_published(self, request, queryset):
        updated = queryset.update(stock=33)
        self.message_user(request, ngettext(
            '%d stock was updateed successfully.',
            '%d stocks was updateed successfully.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = "Update Stock Information to 33"
    actions = [make_published]
    actions = None

    # admin.site.disable_action('delete_selected') #remove delete action

    # fields = ("name", "weight", "brand", "productCategory", "stock")
    fieldsets = (
        ("Basic", {
            'fields': ('productCategory','discount','name')
        }),
        ("Advance Info", {
            'fields': ('keyword', 'brand', 'weight')
        }),
        ('Stock Info', {
            # 'classes': ('collapse',),
            'classes': ('wide','extrapretty'),
            'fields': ('stock', "currentStock", ),
            # 'fields': ('brand', 'stock', "currentStock", "price", "unitPrice"),
            # 'fields': ('brand', ('stock', "currentStock"), ("price", "unitPrice")),
        }),
        ('Price Info', {
            'classes': ('wide','extrapretty'),
            'fields': ("price", "unitPrice",),
            # 'fields': (("price", "unitPrice"),),
        }),
        ('Taxed Info', {
            'classes': ('wide','extrapretty'),
            'fields': ("taxed",),
        }),
    )


    def productAction(self, obj):
        count = obj.name.count("name")
        # https: // realpython.com / customize - django - admin - python /
        url = (
            # reverse("admin:public_product_change") #for edit
            # reverse("admin:public_product_delete") #for delete
            # reverse("admin:public_product_changelist") #for view
            reverse("admin:public_product_add") #for add
            # reverse("admin:public_product_history") #for history
            # reverse("admin:public_product_changelist") + "?" + urlencode({"id": f"{obj.id}"})
        )

        # '{} {}'.format('one', 'two')
        add_url = "/admin/public/product/add/"
        view_url = "/admin/public/product/"
        # edit_url = "/admin/public/product/{}/change/".format(obj.id)
        edit_url = reverse('admin:public_product_change', args=(obj.id,))
        # delete_url = "/admin/public/product/{}/delete/".format(obj.id)
        delete_url = reverse('admin:public_product_delete', args=(obj.id,))
        # history_url = "/admin/public/product/{}/history/".format(obj.id)
        history_url = reverse('admin:public_product_history', args=(obj.id,))
        return format_html("<a class='rec_edit' href='{}' ><b><i>edit</i></b></a> "
                           "\ <a class='rec_delete' href='{}' ><b><i>delete</i></b></a>"
                           "\ <a class='rec_history' href='{}' ><b><i>history</i></b></a>"
                           , edit_url, delete_url, history_url)
    productAction.short_description = "Action"

    #Rename name, currentStock, unitPrice etc field label name
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["name"].label = "Product Name:"
        form.base_fields["currentStock"].label = "Current Stock:"
        form.base_fields["unitPrice"].label = "Unit Price:"
        return form

    # class Media:
    #     css = {
    #         "all": ("my_styles.css","my_styles2.css")
    #     }
    #     # css = {
    #     #     "all": ("my_styles.css","my_styles2.css"),
    #     #     'screen': ('pretty.css',),
    #     #     'tv,projector': ('lo_res.css',),
    #     #     'print': ('newspaper.css',)
    #     # }
    #     js = ("my_code.js","m2.js")
    #     # js = ("js/main.js",)


    # for media like css and javascript
    # @property
    # def media(self):
    #     return forms.Media(css={'all': ('pretty.css',)}, js=('animations.js', 'actions.js'))

    def gallery(request):
        return render(request, "gallery1.html")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.admin_site.admin_view(self.gallery))
        ]
        return my_urls + urls

#To insert data for multiple tables/models from the same page of django admin
# admin.site.register(Product, ProductAdmin)


# @admin.register(ProductInfo)
class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "desc1", "desc2", "desc3", "desc4", "image1","image2","image3","image4")
    empty_value_display = 'No Value'
admin.site.register(ProductInfo, ProductInformationAdmin)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "totalItem","totalTaxed", "discount", "deliveryCost", "totalCost", "user" )
    empty_value_display = 'No Value'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity","totalCost", "cart", "product", "user" )
    empty_value_display = 'No Value'

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "totalItem","totalTaxed", "discount", "deliveryCost", "totalCost" )
    empty_value_display = 'No Value'

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity","totalCost", "invoice", "product", "user" )
    empty_value_display = 'No Value'

@admin.register(DeliveryAddr)
class DeliveryAddrAdmin(admin.ModelAdmin):
    list_display = ("id", "addr_title","p_name", "p_phone", "p_addr1", "p_addr2","area","zip","amount","invoice" )
    empty_value_display = 'No Value'

@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "submitted_at","shippingSlot", "shippingMethod", "note", "onlinePayment" )
    empty_value_display = 'No Value'

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "status","isPaid", "user", "invoice", "deliveryAddr", "orderInfo" )
    empty_value_display = 'No Value'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "amount","order" )
    empty_value_display = 'No Value'






#for varify Product Form
# class ProductAdminForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#     # varify Product=> name attribute
#     def clean_name(self):
#         #Spike can not in product name field
#         if self.cleaned_data["name"] == r"Spike":
#             raise forms.ValidationError("Name is invalid")
#         return self.cleaned_data["name"]
#
#     # varify Product=> description attribute
#     def clean_description(self):
#         #Spike can not in product name field
#         if self.cleaned_data["description"] == r"Spike":
#             raise forms.ValidationError("description is invalid")
#         return self.cleaned_data["description"]

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "description","image_url")
#     list_filter = ("name","description")
#     # search_fields = ("name__startswith",)
#     search_fields = ("name","description")
#     fields = ("name","description","image_url")
#     # list_select_related = ('name',)
#     form = ProductAdminForm
#     # change_list_template = 'p_table.html'
#
#     def changelist_view(self, request, extra_context=None):
#         response = super().changelist_view(  request, extra_context=extra_context,)
#         try:
#             qs = response.context_data["cl"].queryset
#         except (AttributeError, KeyError):
#             return response
#         response.context_data["product_list"] = list(qs.values("id","name","description","image_url").order_by("id"))
#
#         return response

