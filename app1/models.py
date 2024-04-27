from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_choices = (
        ('liters', 'Liters'),
        ('kilograms', 'Kilograms'),
    )
    unit = models.CharField(max_length=20, choices=unit_choices, default='liters')
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"
class Category(models.Model):
    image = models.ImageField(upload_to='category',default='')
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.name}"
