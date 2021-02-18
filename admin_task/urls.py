from django.conf.urls import url
from django.urls import path

from admin_task import views

urlpatterns = [
    # url(r'^public/logout/$', views.logout, name='logout'),
    path('admin/admin_task/analysis/', views.analysis, name="analysis"),# Here must be use path function
    path('admin/admin_task/groupusers/', views.groupUsers, name="groupusers"),# Here must be use path function
    path('admin/admin_task/orders/', views.c_order, name="ad_orders"),# Here must be use path function
    path('admin/admin_task/ad_users/', views.ad_users, name="ad_users"),# Here must be use path function
    path('admin/admin_task/ad_products/', views.ad_products, name="ad_products"),# Here must be use path function
    path('admin/admin_task/ad_products/stock/', views.stock, name="stock"),# Here must be use path function
    # url('', views.PublicPageView.as_view()),
]