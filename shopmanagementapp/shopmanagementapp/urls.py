"""
URL configuration for shopmanagementapp project.

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

from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
schema_view = get_swagger_view(
    title='Shop Management System API Documentation')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_schema/',get_schema_view(title = "SMS API'S",description='Guide for API documentation'),name = 'api_schema'),
    # url for testing apis in swagger ui
    path('api/documentation/',TemplateView.as_view(template_name='docs.html',extra_context = {"schema_url":'api_schema'}),name="swagger_ui"),
    path('api/accounts/',include('users.apis.urls')),
    path("api/product-order/",include('product_order.apis.urls'))

]
