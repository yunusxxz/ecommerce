from django.db import models


class Dimension(models.Model):
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    depth = models.DecimalField(max_digits=6, decimal_places=2)


class MetaInfo(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    barcode = models.CharField(max_length=255)
    qr_code = models.URLField()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    RETURN_POLICY_CHOICES = [('no_return_policy', 'No return policy'),
                             ('7_days_return_policy', '7 days return policy'),
                             ('30_days_return_policy', '30 days return policy'),
                             ('60_days_return_policy', '60 days return policy'),
                             ('90_days_return_policy', '90 days return policy')]

    WARRANTY_INFORMATION_CHOICES = [('no_warranty', 'No warranty'),
                                    ('1_week_warranty', '1 week warranty'),
                                    ('1_month_warranty', '1 month warranty'),
                                    ('3_months_warranty', '3 months warranty'),
                                    ('6_months_warranty', '6 months warranty'),
                                    ('1_year_warranty', '1 year warranty'),
                                    ('2_year_warranty', '2 year warranty'),
                                    ('3_year_warranty', '3 year warranty'),
                                    ('5_year_warranty', '5 year warranty'),
                                    ('lifetime_warranty', 'Lifetime warranty')]

    SHIPPING_INFORMATION_CHOICES = [('ships_overnight', 'Ships overnight'),
                                    ('ships_in_1-2_business_days', 'Ships in 1-2 business days'),
                                    ('ships_in_3-5_business_days', 'Ships in 3-5 business days'),
                                    ('ships_in_1_week', 'Ships in 1 week'),
                                    ('ships_in_2_weeks', 'Ships in 2 weeks'),
                                    ('ships_in_1_month', 'Ships in 1 month')]

    AVAILABILITY_STATUS_CHOICES = [('in_stock', 'In Stock'),
                                   ('out_of_stock', 'Out of Stock'),
                                   ('low_stock', 'Low Stock')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)  # M2M relation for tags
    sku = models.CharField(max_length=20, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.OneToOneField(Dimension, on_delete=models.CASCADE)
    warranty_information = models.CharField(max_length=100, choices=WARRANTY_INFORMATION_CHOICES)
    shipping_information = models.CharField(max_length=100, choices=SHIPPING_INFORMATION_CHOICES)
    availability_status = models.CharField(max_length=50, choices=AVAILABILITY_STATUS_CHOICES)
    return_policy = models.CharField(max_length=100, choices=RETURN_POLICY_CHOICES)
    minimum_order_quantity = models.IntegerField()
    meta = models.OneToOneField(MetaInfo, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()
    reviewer_name = models.CharField(max_length=255)
    reviewer_email = models.EmailField()