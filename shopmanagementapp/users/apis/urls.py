from django.urls import path
# from rest_framework_simplejwt.views import token_obtain_pair,token_refresh
from .views import UserRegisterView,ShopRegisterView,ProductCreateView,ProductUpdateApiView,ShopUpdateApiView,UserShopRetreiveView
urlpatterns = [
    # url for obtaining an access token
    # path("api-token-auth",token_obtain_pair),
    # url for refreshing the token
    # path('refresh-token',token_refresh),
    # url for registering a new user
    path('user-register/',UserRegisterView.as_view()),
    path('shop-register/',ShopRegisterView.as_view()),
    path('product-create-list/<shop>',ProductCreateView.as_view()),
    path('product-retreive-update/<pk>',ProductUpdateApiView.as_view()),
    path('shop-retreive-update/',ShopUpdateApiView.as_view()),
    path("shop-retreive-user_id/<user>",UserShopRetreiveView.as_view())

]
