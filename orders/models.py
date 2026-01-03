# orders/models.py
from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on Delivery'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    
    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UK', 'United Kingdom'),
        ('AU', 'Australia'),
        ('IN', 'India'),
        ('OTHER', 'Other'),
    ]
    
    SHIPPING_METHOD_CHOICES = [
        ('standard', 'Standard Shipping (5-7 days)'),
        ('express', 'Express Shipping (2-3 days)'),
        ('overnight', 'Overnight Shipping (1 day)'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default='US')
    
    shipping_method = models.CharField(max_length=20, choices=SHIPPING_METHOD_CHOICES, default='standard')
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tracking_number = models.CharField(max_length=100, blank=True)
    
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all()) + self.shipping_cost
    
    def get_subtotal(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_items_count(self):
        return sum(item.quantity for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'OrderItem {self.id}'
    
    def get_cost(self):
        return self.price * self.quantity