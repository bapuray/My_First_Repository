"""kulizaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""

from django.conf.urls import include, url
from django.contrib import admin
from kuliza_cart.views import index, about, login_user, logout_user, products, subcategory, \
    category, update_product, delete_product, update_category,delete_category,update_subcategory, \
    delete_subcategory, add_to_cart, cart_checkout, catalog, update_catalog, delete_catalog, my_catalog
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',index),
    url(r'^products/$',products),
    url(r'^products/update/(?P<pk>\d+)/$',update_product),
    url(r'^products/delete/(?P<pk>\d+)/$',delete_product),
    url(r'^category/update/(?P<pk>\d+)/$',update_category),
    url(r'^category/delete/(?P<pk>\d+)/$',delete_category),
    url(r'^cart/add/(?P<pk>\d+)/$',add_to_cart),
    url(r'^cart/checkout/$',cart_checkout),
    url(r'^subcategory/update/(?P<pk>\d+)/$',update_subcategory),
    url(r'^subcategory/delete/(?P<pk>\d+)/$',delete_subcategory),
    url(r'^catalog/$',catalog),
    url(r'^mycatalog/$',my_catalog),
    url(r'^catalog/update/(?P<pk>\d+)/$',update_catalog),
    url(r'^catalog/delete/(?P<pk>\d+)/$',delete_catalog),
    url(r'^category/$',category),
    url(r'^subcategory/$',subcategory),
    url(r'^login/$',login_user),
    url(r'^logout/$',logout_user),
    url(r'^home/$',index),
    url(r'^about_us/$',about),
    # url(r'^polls/', include('pollapp.urls')),
    url(r'^admin/', admin.site.urls),
] 
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

