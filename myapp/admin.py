from django.contrib import admin
from .models import Product_type, Brand, Product, Feature,Product_feature

# Register your models here.
admin.site.register(Product_type)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Product_feature)