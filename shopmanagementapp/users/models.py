from typing import Any
from django.db import models
import random
# Create your models here.
# class usermanager(models.manager):

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class shop(models.Model):
    shop_id = models.CharField(max_length=100,null=False,blank=False)
    shop_name = models.CharField(max_length=100,null = False,blank=False)
    address = models.CharField(max_length=100,null = False,blank=False)
    phone = models.CharField(max_length=100,null = False,blank=False)
    docs = models.FileField(blank=True)
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True)
    def save(self,*args,**kwargs):
        if not self.shop_id:
            shop_id = 'SID'+ str(random.randint(1000, 9999))
            while shop.objects.filter(shop_id=shop_id).exists():
                shop_id = 'SID'+ str(random.randint(1000, 9999))
            self.shop_id = shop_id
        super(shop, self).save(*args, **kwargs)


class user(AbstractBaseUser):
    name = models.CharField(max_length=500,null=False,blank=False)
    phone = models.CharField(max_length=20,null = False,blank = False)
    email = models.EmailField(null = False,blank = False,unique=True)
    password = models.CharField(max_length=500,null=False,blank=False)
    is_consignee = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    shop = models.ForeignKey(shop,on_delete=models.CASCADE)
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


class product(models.Model):
    product_id = models.CharField(max_length=100,null=False,blank=False)
    name = models.CharField(max_length=200,null = False,blank = False)
    shop = models.ForeignKey(shop,on_delete=models.CASCADE)
    measure=(('kgs','kgs'),('units','units'),('litres','litres'))
    measure = models.CharField(max_length=100,choices=measure)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    def save(self,*args,**kwargs):
        if not self.product_id:
            product_id = 'PID'+ str(random.randint(1000, 9999))
            while product.objects.filter(product_id=product_id).exists():
                product_id = 'PID'+ str(random.randint(1000, 9999))
            self.product_id = product_id
        super(product, self).save(*args, **kwargs)





