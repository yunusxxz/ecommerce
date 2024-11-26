from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='shop_index'),
    path("category/<str:slug>", views.category_index, name="shop_category"),
    path("brand/<str:slug>", views.brand_index, name="shop_brand"),
]