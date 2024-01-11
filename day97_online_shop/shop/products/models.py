from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits = 5, decimal_places = 2)
    product_description = models.CharField(max_length = 500)
    product_image = models.ImageField(upload_to = "photos")
    available_amount = models.IntegerField()

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ordered_products = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)



