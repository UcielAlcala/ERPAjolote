# erp_backend/inventories/models.py

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from erp_backend.batch_number.models import BatchNumber
from erp_backend.sku.models import SKU

class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=0)
    item_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=7)
    content_object = GenericForeignKey('content_type', 'item_id')
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    batch_number = models.ForeignKey(BatchNumber, on_delete=models.CASCADE, null=True, blank=True, related_name='inventory_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content_object} in {self.warehouse}"
    
    def save(self, *args, **kwargs):
        # Si no se ha asignado un número de lote, generar uno
        if not self.batch_number:
            sku_instance = SKU.objects.get(content_type=self.content_type, item_id=self.item_id)
            batch_number_instance = BatchNumber.objects.create(sku=sku_instance)
            self.batch_number = batch_number_instance
        super().save(*args, **kwargs)