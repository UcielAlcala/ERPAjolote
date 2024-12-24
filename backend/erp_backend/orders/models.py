# erp_backend/orders/models.py

from django.db import models
from django.contrib.auth.models import User
from erp_backend.final_products.models import FinalProduct
from erp_backend.printed_pieces.models import PrintedPiece

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    final_product = models.ForeignKey(FinalProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.FloatField()  # costo total del producto en la orden
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OrderItem {self.id} for Order {self.order.id}"
    
class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='details')
    printed_piece = models.ForeignKey(PrintedPiece, on_delete=models.CASCADE)
    required_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    material_needed = models.FloatField()
    print_time_needed = models.DurationField()
    cost = models.FloatField()  # costo del detalle del pedido
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OrderDetail {self.id} for OrderItem {self.order_item.id}"