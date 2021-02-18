import os

from django.apps import AppConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = "/home/shoumitro/Documents/html_ex/FoodShop_MS/src/foodshop"


#https://docs.djangoproject.com/en/3.1/ref/applications/
class PublicConfig(AppConfig):
    name = 'public'
    verbose_name = "Client Side Information"
    path = BASE_DIR + "/public/"
    label = "public"
