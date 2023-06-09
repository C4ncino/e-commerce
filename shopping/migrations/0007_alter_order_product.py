# Generated by Django 4.2 on 2023-05-15 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_brand'),
        ('shopping', '0006_remove_cart_products_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
