from django.shortcuts import render
import requests as req

from .models import Brand, Category
from .templatetags.custom_filters import to_slug


# Create your views here.
def index(request):
    res = req.get("https://dummyjson.com/products?limit=0")
    if res.status_code == 200:
        data = res.json()

        # b_set = {x['brand'] for x in data['products'] if 'brand' in x.keys()}
        # brands = [Brand(name=x) for x in b_set]
        #
        # c_set = {x['category'] for x in data['products'] if 'category' in x.keys()}
        # categories = [Category(name=x) for x in c_set]
        #
        # Brand.objects.bulk_create(brands)
        # Category.objects.bulk_create(categories)

        for p in data['products']:
            p['discountedPrice'] = p['price'] * (100 - p['discountPercentage']) / 100

        return render(request, 'shop/index.html', data)
    else:
        return render(request, 'shop/index.html')


def brand_index(request, slug=None):
    print(slug)
    res = req.get("https://dummyjson.com/products?limit=0")
    if res.status_code == 200:
        data = res.json()

        products = []
        for p in data['products']:
            p['discountedPrice'] = p['price'] * (100 - p['discountPercentage']) / 100
            if 'brand' in p.keys() and to_slug(p['brand']) == slug:
                products.append(p)

        data['products'] = products
        return render(request, 'shop/index.html', data)
    else:
        return render(request, 'shop/index.html')


def category_index(request, slug=None):
    print(slug)
    res = req.get(f"https://dummyjson.com/products/category/{slug}?limit=0")
    if res.status_code == 200:
        data = res.json()

        for p in data['products']:
            p['discountedPrice'] = p['price'] * (100 - p['discountPercentage']) / 100

        return render(request, 'shop/index.html', data)
    else:
        return render(request, 'shop/index.html')