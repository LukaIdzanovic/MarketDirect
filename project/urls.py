"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from app.views import home, profile, products, shops, add_new_products, remove_product

urlpatterns = [
    path('', home, name='homepage'),
    path('admin/', admin.site.urls),
    path('profile/', profile, name="profile" ),
    path('accounts/', include("django.contrib.auth.urls")),
    path('products/',products, name='products'),
    path('shops/',shops, name='shops'),
    path('products/addNewProduct', add_new_products, name="addNewProduct"),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
]