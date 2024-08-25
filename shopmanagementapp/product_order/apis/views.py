from .serializers import ProductOrderSerializer
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from product_order.models import product_order
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE


class ProductOrderCreationView(CreateAPIView):
    serializer_class = ProductOrderSerializer
    queryset = product_order.objects.all()
    # def get_queryset(self):
    #     query_params = self.request.query_params
    #     shop_id = query_params.get('shop', False)
    #     if shop_id:
    #         return product_order.objects.filter(shop_id=shop_id)
    #     else:
    #         return {"message":"Shop ID not given","status":HTTP_406_NOT_ACCEPTABLE}
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ProductOrderUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductOrderSerializer
    queryset = product_order.objects.all()
    # def get_queryset(self):
    #     query_params = self.request.query_params
    #     shop_id = query_params.get('shop', False)
    #     if shop_id:
    #         return product_order.objects.filter(shop_id=shop_id)
    #     else:
    #         return {"message":"Shop ID not given","status":HTTP_406_NOT_ACCEPTABLE}
