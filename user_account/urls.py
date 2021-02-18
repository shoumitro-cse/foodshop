from django.conf.urls import url
from django.urls import path

from user_account import views

urlpatterns = [
    url(r'user/dashboard', views.dashboard, name='dashboard'), # Notice the URL has been named
    url(r'user/profile', views.profile, name='profile'), # Notice the URL has been named
    path('user/order_view/<int:id>', views.order_view), # Here must be use path function
    url(r'user/order', views.order, name='order'), # Notice the URL has been named
    url(r'user/wishlist', views.wishlist, name='wishlist'), # Notice the URL has been named
    url(r'user/comment_review', views.comment_review, name='comment_review'), # Notice the URL has been named
    url(r'user/help_support', views.help_support, name='help_support'), # Notice the URL has been named
    url(r'user/settings', views.settings, name='settings'), # Notice the URL has been named
    url(r'user/change_password', views.change_password, name='change_password'), # Notice the URL has been named
    url(r'user/addresses', views.addresses, name='addresses'), # Notice the URL has been named
    # url(r'user/order', views.orderPage.as_view(), name='order'), # Notice the URL has been named
]