from urllib.parse import urlparse, urlunparse
from django.http import QueryDict

from django.shortcuts import render, redirect
from django.views.generic import TemplateView # Import TemplateView

from public.models import Product


# Create your views here.

def c_order(request):
    return render(request, "admin_orders.html")

def ad_products(request):
    return render(request, "admin_products.html")

def ad_users(request):
    return render(request, "users.html")

def groupUsers(request):
    return render(request, "admin_user.html")

def analysis(request):
    return render(request, "analysis.html")

def stock(request): # for list and dictionary
    #here values return => list(dictionary)
    product_dict_list = Product.objects.all().values("id", "name", "stock", "currentStock")
    return render(request, "stock.html", {"product_dict_list":product_dict_list})

#def stock(request): #for list and typle
#    #here values return => list(tuple)
#    product_list = Product.objects.all().values_list("id", "name", "stock", "currentStock")
#    return render(request, "stock.html", {"product_list":product_list})