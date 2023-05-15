from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    date = models.DateField(null=True, blank=True)

    def __str__(self) :
        return self.user.username

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # def __str__(self) :
    #     return self.cart.user.username + ':' + self.product.name