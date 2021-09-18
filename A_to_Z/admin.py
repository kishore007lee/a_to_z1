from django.contrib import admin
from .models import shops,products,trending_products
# Register your models here.

admin.site.register(shops)
admin.site.register(products)
admin.site.register(trending_products)

