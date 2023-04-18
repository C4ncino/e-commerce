from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__(self) :
        return self.name