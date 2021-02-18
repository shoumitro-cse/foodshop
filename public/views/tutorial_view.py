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
# import public.controlers

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

#class view

#for base class view
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/base/#django.views.generic.base.View.as_view

#http://127.0.0.1:8000/mine/
# class MyView(View):
class MyView(TemplateView):

    # ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    # paginate_by = 2
    template_name = "gallery1.html" # http://127.0.0.1:8000/mine/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_dict_list'] = productData.getTotalProduct()
        return context

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, post!')

    def put(self, request, *args, **kwargs):
        return HttpResponse('Hello, Put!')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('Hello, Delete!')

# http://127.0.0.1:8000/userlistview/
class UserListView(ListView):
    allow_empty = True
    model = None
    paginate_by = None
    paginate_orphans = 0
    context_object_name = None
    paginator_class = Paginator
    page_kwarg = 'page'
    ordering = "id"

    # model = Product
    model = Users
    paginate_by = 2  # if pagination is desired
    # paginator = Paginator(queryset, 2)
    template_name = "gallery.html"
    template_name = "user_fake/user_list_view.html"

    #these two same
    # queryset = None
    # queryset = Users.objects.all()
    # def get_queryset(self):
    #     return Users.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['product_dict_list'] = productData.getTotalProduct()
        return context

# http://127.0.0.1:8000/user/4/show/
class UserDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "user_fake/user_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Users.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context

    def get_queryset(self):
        return Users.objects.all()


# Generic editing views
# http://127.0.0.1:8000/user/sendemail/
class UserSendEmail(FormView):
    template_name = 'user_fake/sendemail.html'
    form_class = UsersForm
    success_url = '/user/sendemail/'

    #if form is vaild it send a email
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)



# http://127.0.0.1:8000/user/add/
class UserCreate(CreateView):
    # model = Product
    model = Users
    # inlines = [Login]
    # fields = ['fullname']
    fields = "__all__"
    template_name = "user_fake/create.html"
    success_url = '/user/add/'

# http://127.0.0.1:8000/user/1/
class UserUpdate(UpdateView):
    # model = Product #http://127.0.0.1:8000/user/6000000/
    model = Users
    # fields = ['fullname']
    fields = "__all__"
    template_name = "user_fake/update.html"
    success_url = '/user/add/'

# http://127.0.0.1:8000/user/4/delete/
class UserDelete(DeleteView):
    model = Users
    success_url = reverse_lazy('user-add')
    template_name = "user_fake/delete.html"


# http://127.0.0.1:8000/publishers/
# class AcmeProductList(DetailView):
class AcmeProductList(ListView):
    # paginate_by = 2
    model = Product
    context_object_name = 'prodict_dict'
    # queryset = Product.objects.all()
    template_name = 'product.html'

    #these two same result
    # queryset = productData.getProductById(6000002)
    def get_queryset(self):
        return productData.getProductById(6000002);


class PublicPageView(TemplateView):
    template_name = "gallery1.html"
ppv = PublicPageView()
# ppv.as_view
ppv.template_name = "g.html"
# ppv.content_type
# ppv.get_template_names()
# ppv.extra_context
# ppv.http_method_names
# ppv.response_class
# ppv.template_engine
# ppv.kwargs

#######################--For Tutorials--##########################
from django.http import HttpResponse
from django.template import RequestContext, Template

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def client_ip_view(request):
    template = Template("<h1 class='title'>{{ title }}: {{ ip_address }}</h1>")
    context = RequestContext(request, {# class RequestContext(request, dict_=None, processors=None)¶
        'title': 'Your IP Address',
    }, [ip_address_processor])
    return HttpResponse(template.render(context))

class TutorialCollection:

    def __init__(self):
        pass

    # def tutorial(self, request):
    #     return client_ip_view(request)


    def tutorial(self, request):
        return render(request, "tutorial.html")
        # return TemplateResponse(request, "tutorial.html")

      # create a pdf
    def create_pdf(self, request):
        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(50, 50, "Hello world.")

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

    # JsonResponse inherit HttpResponse
    # def tutorial(self, request):
    #     response = JsonResponse({'foo': 'bar'})
    #     return response

# def tutorial(request):
#     return client_ip_view(request)

# def tutorial(request):
#     return render(request, "tutorial.html")
#################################################