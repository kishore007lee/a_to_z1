from django.db import models

# Create your models here.
class product_details(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    img = models.ImageField(upload_to= 'pics')
    desc = models.TextField()



class products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    img = models.ImageField(upload_to= 'pics')

class product_details1(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    img = models.ImageField(upload_to= 'pics')
    desc = models.TextField()


class shops(models.Model):
    shop_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to= 'pics')
    desc = models.TextField()
    offer=models.BooleanField()

