from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .serializers import UserRegisterSerializer,ShopRegisterSerializer,ProductCreateSerializer
from users.models import user,shop,product
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

# view for creating a new user object
class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = user.objects.all()
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)
    

class ShopRegisterView(CreateAPIView):
    serializer_class = ShopRegisterSerializer
    queryset = shop.objects.all()
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = ShopRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)

class ProductCreateView(ListCreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = product.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)
    def get_queryset(self):
        query_params = self.request.query_params
        shop_id = query_params.get('shop', False)
        if shop_id:
            return product.objects.filter(shop_id=shop_id)
        else:
            return product.objects.all()

class ProductUpdateApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset = product.objects.all()
    serializer_class = ProductCreateSerializer

class ShopUpdateApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset = shop.objects.all()
    serializer_class = ShopRegisterSerializer
    def get_queryset(self):
        query_params = self.request.query_params
        shop_id = query_params.get('shop', False)
        if shop_id:
            return shop.objects.get(shop_id=shop_id)
        else:
            return shop.objects.all()
        
class UserShopRetreiveView(RetrieveAPIView):
    serializer_class = ShopRegisterSerializer
    def get(self, request, *args, **kwargs):
        query_params = self.request.query_params
        user_id = query_params.get('user', False)
        if user_id:
            user_obj = user.objects.get(id = user_id)
            return user_obj.shop
        return super().get(request, *args, **kwargs)
