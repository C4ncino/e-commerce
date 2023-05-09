from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='order')
    date = models.DateField(null=True, blank=True)