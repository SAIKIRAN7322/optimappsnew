from rest_framework import serializers
from users.models import user,shop,product
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 200,write_only = True)
    class Meta:
        model = user
        fields= ["id",'name','email','password','phone','is_consignee','is_owner','shop']
        read_only_fields=['id']

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class ShopRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields= ['id',"shop_id",'shop_name','phone','address']
        read_only_fields=['id','shop_id']

    

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length = 200,required =True)
#     password = serializers.CharField(max_length = 200,required = True)

class ProductCreateSerializer(serializers.Serializer):
    class Meta:
        model = product
        fields = ['id','product_id','name','shop','image']
        read_only_fields = ['product_id','id']