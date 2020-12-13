from django.db import models


class Product_type(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, null=False, unique=True)
    brand_type = models.ForeignKey(Product_type, on_delete=models.SET_NULL, null=True)
    brand_info = models.TextField(null=False)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=255, null=False, unique=True)
    product_slug = models.SlugField(unique=True, blank=True, null=True)
    product_title = models.CharField(max_length=255, null=True)
    product_info = models.TextField(null=False)
    product_description = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    product_type = models.ForeignKey(Product_type, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(max_length=100, default="publish")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Feature(models.Model):
    feature_name = models.CharField(max_length=255, null=False)
    product_type = models.ForeignKey(Product_type, on_delete=models.SET_NULL, null=True)
    feature_has_value = models.CharField(max_length=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feature_name


class Product_feature(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_feature_value = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
