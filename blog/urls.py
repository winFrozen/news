from django.urls import path
from .views import index, single, contact, category, newdetailview, products, productdetailview, tnewsdetailview

urlpatterns = [
    path("index/", index, name='index'),
    path("single/", single, name='single'),
    path("contact/", contact, name='contact'),
    path("category/", category, name='category'),
    path("new/<int:id>", newdetailview, name='new_detail_view'),
    path("products/", products, name='products'),
    path("products/<slug:product>", productdetailview, name='product_detail_view'),
    path("tnews/<slug:tnews>", tnewsdetailview, name='tnews_detail_view'),

    ]
