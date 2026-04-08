from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100, default="fashion")
    drama_name = models.CharField(max_length=100, default="K-drama")

    def __str__(self):
        return self.name