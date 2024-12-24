from django.db import models
from django.utils import timezone
from erp_backend.materials.models import Material
from erp_backend.supplier.models import Supplier

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pendiente'),
        ('Approved', 'Aprobado'),
        ('Received', 'Recibido'),
        ('Closed', 'Cerrado'),
        ('Canceled', 'Cancelado'),
    ]

    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField(default=timezone.now)
    expected_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    total_cost = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Purchase Order {self.id} from {self.supplier.name}"

    def calculate_total_cost(self):
        total_cost = sum(item.total_cost for item in self.items.all())
        self.total_cost = total_cost
        self.save()


class PurchaseOrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items', blank=True)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantity = models.FloatField()
    cost_per_unit = models.FloatField()
    total_cost = models.FloatField()
    received_quantity = models.FloatField(default=0.0)
    received_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.material.name} in Order {self.purchase_order.id}"

    def save(self, *args, **kwargs):
        self.total_cost = self.quantity * self.cost_per_unit
        super().save(*args, **kwargs)
        self.purchase_order.calculate_total_cost()
