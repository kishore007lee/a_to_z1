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

class lovis1(models.Model):
    tshirt=models.ImageField(upload_to= 'pics')
    tshirt_name=models.CharField(max_length=100)
    tshirt_price=models.TextField()
    shirt = models.ImageField(upload_to='pics')
    shirt_name = models.CharField(max_length=100)
    shirt_price = models.TextField()
    pant= models.ImageField(upload_to='pics')
    pant_name = models.CharField(max_length=100)
    pant_price = models.TextField()

class lovis2(models.Model):
    products_name1=models.TextField()
    products_name2= models.TextField()
    products_price=models.IntegerField()
    products_img=models.ImageField(upload_to= 'pics')

class AM_plasma(models.Model):
    products_name1=models.TextField()
    products_name2= models.TextField()
    products_price=models.IntegerField()
    products_img=models.ImageField(upload_to= 'pics')
