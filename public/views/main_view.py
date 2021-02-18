import json
from urllib.parse import urlparse, urlunparse

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import QueryDict, HttpResponse, HttpRequest, JsonResponse

from django.shortcuts import render, redirect
from django.template.response import TemplateResponse, SimpleTemplateResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, \
    CreateView, FormView  # Import TemplateView
from django.views.generic.detail import SingleObjectMixin

from  public.controlers import ProductData, Shopping, UserData
from public.models import Product

# Create your views here.
from public.models import Login, Users, ProductInfo
from public.forms import UsersForm

#for pdf
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

productData = ProductData()
shopping = Shopping()
userData = UserData()


#https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
# Pagination with Class-Based views
class Gallery(ListView):
    # model = Product
    model = ProductInfo
    ordering = "-id"
    paginate_by = 6
    template_name = "gallery.html" # Default: <app_label>/<model_name>_list.html
    context_object_name = 'product_list'  # Default: object_list
    queryset = ProductInfo.objects.all()  # Default: Model.objects.all()


#https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
#Pagination with Function-Based views
def gallery_index(request):
    product_list = ProductInfo.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 7)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'gallery2.html', { 'products': products })


class CustomTemplateResponse(TemplateResponse):
    pass

# class PublicView(TemplateView):
class PublicView:

    def __init__(self):
        pass

    def fake(self, response):
        return "fake"

    def gallery(self, request):
        # data = productData.getTotalProductByCategory()
        # json_data = json.dumps(productData.getTotalProductByCategory())
        # return render(request, "gallery1.html", {"product_dict_list":json_data})

        # queryset = productData.getTotalProduct()
        queryset = ProductInfo.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 6)

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        return TemplateResponse(request, "gallery2.html", {"product_dict_list":product, "products":product})

    # TemplateResponse class inherit HttpResponse class
    def productView(self, request, product_id):
        prodict_dict = productData.getProductById(product_id)
        response = CustomTemplateResponse(request, "product.html", {'prodict_dict':prodict_dict})
        # response.add_post_render_callback(self.fake)
        # response.set_cookie("foodshop_cookie","ProductView"
        # print(response.cookies)
        # print("Hello")
        return response

    def cart(self, request):
        return render(request, "cart.html")

    def cart_item(self, request):
        email = userData.getSessionUserEmail(request)
        if email:
            user_obj = userData.getUserObj(user_email=email)
            if user_obj:
                cart_list = shopping.getCart(user_obj)
                return HttpResponse("<div class='item_text'>{} item(s)</div><div class='cart_item_price'>TK{}</div>".format(cart_list.totalItem, cart_list.totalCost))
            else:
                print("User Object is not found")
        else:
            return HttpResponse("<div class='item_text'>No item</div><div class='cart_item_price'>TK0.00</div>")

    def addTocart(self, request, product_id):
        if request.session.has_key('username'):
            user_email = request.session['username']
            shopping.addTocart(product_id, user_email)
        return HttpResponse()

    def contact(self, request):
        return render(request, "contact.html")

    def pricing(self, request):
        return render(request, "pricing.html")

    def track_order(self, request):
        return render(request, "track_order.html")

    def logout(self, request):
        try:
            del request.session['username']
            return redirect("/foodshop")
        except:
            return redirect("/foodshop")
            pass

    # @require_http_methods(["GET", "POST"])
    def signin(self, request):
        if request.method == 'POST':
            #<QueryDict: {
            #  'csrfmiddlewaretoken': ['VkQG5RlMMdIc0GEFsMYhgSZZW74MKjE1BSpHYLWPZwKaWUtOCDCVa1oVcwIzOuNu'],
            #  'email': ['jack@gmail.com'],
            #  'password': ['Bd12345678']
            #  }>
            # print(request.POST)
            email = request.POST['email']
            password = request.POST['password']
            l = Login.objects.filter(user_name=email, u_password=password)
            # print(l[0].user_name)
            if not l:
                try:
                    del request.session['username']
                except:
                   print("Can't any user")
            else:
                # print(l[0].user_name)
                request.session['username'] = email
            return redirect("/foodshop")


    # @require_http_methods(["GET", "POST"])
    def check_email(self, request):
        # email = require_GET("email")
        # email = require_POST("email")
        # email = require_safe("email") #Decorator to require that a view only accepts the GET and HEAD methods
        email = request.GET['email']
        if email != "":
            l = Login.objects.filter(user_name=email)
            user = False;
            if not l:
                user = False;
            else:
                user = True;
        else:
            user = False
        return render(request, "email_ck.html", {"user":user})

    # @require_http_methods(["GET", "POST"])
    def user_check(self, request):
        email = request.GET['email']
        password = request.GET['password']
        if email != "" and password != "":
            l = Login.objects.filter(user_name=email, u_password=password)
            user = False;
            if not l:
                user = False;
            else:
                user = True;
        else:
            user = False
        return render(request, "email_ck.html", {"user":user})

    # @require_http_methods(["GET", "POST"])
    def signup(self, request):
        if request.method == 'GET':
            g_fullname = request.GET['fullname']
            g_email = request.GET['email']
            g_password = request.GET['password']
            g_retype_password = request.GET['retype_password']
            try:
                if len(g_password) < 8 and g_password != g_retype_password:
                    print("\n\nPassword are not match.\n\n")
                    return redirect("/foodshop")

                user_ck = Login.objects.filter(user_name=g_email)
                if user_ck:
                    print("\n\nUser Alrady Exist\n\n")
                    return redirect("/foodshop")

                if g_fullname != "" and g_email != "" and g_password != "" and g_retype_password != "":
                    u = Users(fullname=g_fullname, email=g_email)
                    u.save()
                    u = Users.objects.order_by("-id")
                    l = Login(user=u[0], user_name=g_email, u_password=g_password, u_re_password=g_retype_password)
                    l.save()
                else:
                    print("\n\nInput Field is Empty or User Alrady Exist\n\n")

                return redirect("/foodshop")
            except:
                print("User Can not SignUp")
                return redirect("/foodshop")


# parsed_url = urlparse('https://www.example.com/path?1=a&2=b#fragment')
parsed_url = urlparse('https://www.example.com/path?name=shoumitro&email=shoumitro26@gmail.com#fragment')
queries = QueryDict(parsed_url.query, mutable=True)
# queries
# queries['name']
# print(queries['email'])

# queries.update({'1': 'c', '3': 'd'})
# new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, queries, parsed_url.fragment))
