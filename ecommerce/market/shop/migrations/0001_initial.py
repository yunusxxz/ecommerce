# Generated by Django 5.1.3 on 2024-11-25 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='MetaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('barcode', models.CharField(max_length=255)),
                ('qr_code', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('stock', models.IntegerField()),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('warranty_information', models.CharField(choices=[('lifetime_warranty', 'Lifetime warranty'), ('6_months_warranty', '6 months warranty'), ('1_year_warranty', '1 year warranty'), ('5_year_warranty', '5 year warranty'), ('2_year_warranty', '2 year warranty'), ('1_month_warranty', '1 month warranty'), ('1_week_warranty', '1 week warranty'), ('no_warranty', 'No warranty'), ('3_year_warranty', '3 year warranty'), ('3_months_warranty', '3 months warranty')], max_length=100)),
                ('shipping_information', models.CharField(choices=[('ships_in_3-5_business_days', 'Ships in 3-5 business days'), ('ships_in_2_weeks', 'Ships in 2 weeks'), ('ships_overnight', 'Ships overnight'), ('ships_in_1-2_business_days', 'Ships in 1-2 business days'), ('ships_in_1_week', 'Ships in 1 week'), ('ships_in_1_month', 'Ships in 1 month')], max_length=100)),
                ('availability_status', models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('low_stock', 'Low Stock'), ('in_stock', 'In Stock')], max_length=50)),
                ('return_policy', models.CharField(choices=[('90_days_return_policy', '90 days return policy'), ('no_return_policy', 'No return policy'), ('60_days_return_policy', '60 days return policy'), ('7_days_return_policy', '7 days return policy'), ('30_days_return_policy', '30 days return policy')], max_length=100)),
                ('minimum_order_quantity', models.IntegerField()),
                ('thumbnail', models.URLField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
                ('dimensions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.dimension')),
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.metainfo')),
                ('tags', models.ManyToManyField(blank=True, related_name='products', to='shop.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('reviewer_name', models.CharField(max_length=255)),
                ('reviewer_email', models.EmailField(max_length=254)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.product')),
            ],
        ),
    ]