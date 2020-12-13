from django.urls import path
from .views import Insert_product,Product_list

urlpatterns = [
    path('insert-product/',Insert_product.as_view(),name="insert_product"),
    path('list/',Product_list.as_view(),name="product-list"),
]