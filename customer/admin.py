from django.contrib import admin
from .models import Customer    
from .models import Product
from .models import supplier
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name','contact_number','email','address')
    search_fields = ('customer_name', 'contact_number', 'email', 'address')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','description')
    search_fields = ('product_name', 'price', 'description')
    
@admin.register(supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id','supplier_name','contact_number','email','address')
    search_fields = ('supplier_name', 'contact_number', 'email', 'address')