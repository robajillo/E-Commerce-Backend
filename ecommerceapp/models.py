from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField




class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=100,choices=[('TSHIRT', 'T-Shirt'), ('SHOES', 'Shoes'),('JEAN', 'jean'),('SHRUGS', 'Shrugs')])


    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_details")
    username = models.CharField(max_length=100)
    order_id = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="order_details")
    address_type = models.CharField(max_length=100,choices=[('BILLING', 'Billing'), ('SHIPPING', 'Shipping')])
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    numincart = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="cart")

    def __str__(self):
        return self.username