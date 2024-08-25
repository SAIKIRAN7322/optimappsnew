from django.db import models
from users.models import  shop,product
# Create your models here.
class product_available(models.Model):
    shop = models.ForeignKey(shop,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    selling_price = models.FloatField(null=True,blank=True)
    cost_price = models.FloatField(null=True,blank=True)
    quantity_available = models.FloatField(null=True,blank=True)
