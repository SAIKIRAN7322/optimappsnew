from rest_framework import serializers
from product_order.models import product_order

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_order
        fields= ['id',"shop",'product','quantity_required','order_date_time']
        read_only_fields=['id','order_date_time']
    def validate(self, attrs):
        print('validate')
        return super().validate(attrs)

class ProductOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_order
        fields= ['id',"shop",'product','quantity_required','order_date_time']
        read_only_fields=['order_date_time']
    def validate(self, attrs):
        print('validate')
        return super().validate(attrs)