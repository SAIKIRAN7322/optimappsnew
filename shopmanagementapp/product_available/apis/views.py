from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ProductAvailableCreateSerializer,ProductAvailableUpdateSerializer
from product_available.models import product_available

class ProductAvailableCreateView(CreateAPIView):
    serializer_class = ProductAvailableCreateSerializer
    queryset = product_available.objects.all()

class ProductAvailableUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductAvailableUpdateSerializer
    queryset = product_available.objects.all()

    def get_queryset(self):
        if self.product_id and self.shop_id:
            return product_available.objects.filter(product_product_id=self.product_id,shop_shop_id = self.shop_id)
    
    