from .views import ProductAvailableUpdateView,ProductAvailableCreateView
from django.urls import path
urlpatterns=[
path('product-available/create',ProductAvailableCreateView.as_view()),
path('product-available/update',ProductAvailableUpdateView.as_view())

]