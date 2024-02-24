"""
URL configuration for Shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('profile/',profile,name='profile'),
    path('login/',login_user,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_user,name='logout'),
    path('product/<str:cat>',product_list,name='product'),
    path('productinfo/<int:pk>',product_info,name='productinfo'),
    path('cart/<int:id>',cart,name='cart'),
    path('cart/',cartall,name='cart'),
    path('qntyadd/<int:id>',qntyadd,name='qntyadd'),
    path('qntysub/<int:id>',qntysub,name='qntysub'),
    path('remove/<int:id>',removedish,name='remove'),
    path('search/',search,name='search'),
    path('order/',order,name='order'),
    path('payment/',payment,name='payment'),
    path('orderhistory/',orderhistory,name='orderhistory'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
