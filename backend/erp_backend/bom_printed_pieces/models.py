from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from erp_backend.final_products.models import FinalProduct
from erp_backend.materials.models import Material
from erp_backend.printed_pieces.models import PrintedPiece

class BOMPrintedPiece(models.Model):
    id = models.AutoField(primary_key=True)
    final_product = models.ForeignKey(FinalProduct, on_delete=models.CASCADE, related_name='bom_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.IntegerField()
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"BOM for {self.final_product.name}"

    def save(self, *args, **kwargs):
        if isinstance(self.content_object, PrintedPiece):
            self.cost = self.content_object.cost
        elif isinstance(self.content_object, Material):
            self.cost = self.content_object.cost_per_unit
        super().save(*args, **kwargs)
