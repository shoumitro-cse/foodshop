from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

# from public.views.main_views import PublicView, TutorialCollection, AcmeProductList, MyView, UserCreate, UserUpdate, UserDelete, UserSendEmail, UserDetail, UserListView, Gallery, gallery_index
from public.views import *

tutorialCollection =  TutorialCollection()
publicView =  PublicView()
urlpatterns = [
    path('user/sendemail/', UserSendEmail.as_view(), name='user-sendemail'),
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('user/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),

    path('mine/', MyView.as_view(), name='my-view'),
    path('publishers/', AcmeProductList.as_view()),

    # path('user/show/', UserDetail.as_view()),
    path('user/<int:pk>/show/', UserDetail.as_view()),
    path('userlistview/', UserListView.as_view(), name='user-list'),

    path('create_pdf/', tutorialCollection.create_pdf, name='create_pdf'),


    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path(r'foodshop/public/user_check/', publicView.user_check, name='user_check'),
    path(r'foodshop/public/check_email/', publicView.check_email, name='check_email'),
    path(r'public/track_order/', publicView.track_order, name='track_order'),
    path(r'public/pricing/', publicView.pricing, name='pricing'),
    path(r'public/contact/', publicView.contact, name='contact'),
    path(r'public/cart/', publicView.cart, name='cart'),
    path(r'public/signin/', publicView.signin, name='signin'),
    path(r'public/signup/', publicView.signup, name='signup'),
    path(r'public/logout/', publicView.logout, name='logout'),
    path(r'public/cart_item', publicView.cart_item, name='cart_item'),
    path(r'public/tutorial', tutorialCollection.tutorial, name='tutorial'),
    # url(r'^public/tutorial', views.tutorial, name='tutorial'),
    path('public/add_cart/<int:product_id>', publicView.addTocart),# Here must be use path function
    path('public/product/<int:product_id>', publicView.productView, name="product"),# Here must be use path function
    url(r'^home/$', Gallery.as_view(), name='home'), # Notice the URL has been named
    path(r'foodshop/', Gallery.as_view(), name='foodshop'), # Notice the URL has been named
    # path('', Gallery.as_view(), name="gallery"),
    # path('', gallery_index, name="gallery"),
    # path('', publicView.gallery, name="gallery"),
    url(r'^$', publicView.gallery, name="gallery"), #find empty slash
    # url('', views.PublicPageView.as_view()),
]