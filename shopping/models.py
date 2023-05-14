from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='order')
    date = models.DateField(null=True, blank=True)