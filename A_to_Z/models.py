from django.db import models

# Create your models here.


class shops(models.Model):
    shop_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to= 'pics')
    city = models.TextField()


class products(models.Model):
    shop_id = models.IntegerField()
    shop_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to= 'pics')
    category= models.TextField()
    product_name = models.TextField()
    product_desc = models.TextField()
    product_price=models.IntegerField()


class trending_products(models.Model):
    shop_id = models.IntegerField()
    shop_name = models.CharField(max_length=100)
    product_name = models.TextField()
    img = models.ImageField(upload_to='pics')
    product_price = models.IntegerField()
