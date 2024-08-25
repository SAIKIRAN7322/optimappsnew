from product_available.models import product_available
from rest_framework import serializers

class ProductAvailableCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_available
        fields = '__all__'

class  ProductAvailableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_available
        fields = ['id','selling_price','cost_price','quantity_available']
        extra_kwargs = {
            'product_id': {'required': True},
            'shop_id': {'required': True}
        }
