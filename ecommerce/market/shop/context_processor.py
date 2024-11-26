from .models import Brand, Category


def shop_data(request):
    return {
        "brands": Brand.objects.all(),
        "categories": Category.objects.all()
    }

