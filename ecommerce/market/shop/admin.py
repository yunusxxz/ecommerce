from django.contrib import admin

from .models import Brand, Category, Dimension, MetaInfo, Tag, Product, ProductImage, Review

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Dimension)
admin.site.register(MetaInfo)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)