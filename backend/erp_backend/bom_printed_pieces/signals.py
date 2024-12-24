from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BOMPrintedPiece
from erp_backend.final_products.models import FinalProduct

@receiver(post_save, sender=BOMPrintedPiece)
@receiver(post_delete, sender=BOMPrintedPiece)
def update_final_product_cost(sender, instance, **kwargs):
    final_product = instance.final_product
    bom_items = BOMPrintedPiece.objects.filter(final_product=final_product)
    
    total_cost = sum(item.cost for item in bom_items)
    final_product.total_cost = total_cost
    final_product.save()
