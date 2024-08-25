from django.db import models
from users.models import  shop,product

# Create your models here.
class product_order(models.Model):
    shop = models.ForeignKey(shop,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity_required = models.FloatField(null=True,blank=True)
    order_date_time = models.DateTimeField(auto_now_add=True)





