"""foodshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'FoodShop'
admin.site.site_title = 'Food Shop admin'
#admin.site.site_url = 'http://127.0.0.1:8000'
admin.site.site_url = '/'
admin.site.index_title = 'Admin Dashboard'
admin.empty_value_display = '**Empty**'


#for media file
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#for static file
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path(r'admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # path(r'admin', admin.site.urls),

    #Function views
    #path('', public_view.index),

    #Class-based views
    #these url load from public app
    #url('', public_view.HomePageView.as_view()),
    #url(r'^home/$', public_view.HomePageView.as_view(), name='home'),

    #Including another URLconf
    url(r'^', include('user_account.urls')),  # tell django to read user_account/main_url.py in user_account app
    url(r'^', include('admin_task.urls')),  # tell django to read public/main_url.py in public app
    url(r'^', include('public.urls')),  # tell django to read public/main_url.py in public app
]

