from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True , blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.customer_name
    

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.product_name
    
class supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True , blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.supplier_name