from django.db import models
from datetime import datetime
from erp_backend.sku.models import SKU

class BatchNumber(models.Model):
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='batches')
    batch_number = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.batch_number

    def save(self, *args, **kwargs):
        if not self.batch_number:
            self.batch_number = self.generate_batch_number()
        super().save(*args, **kwargs)

    def generate_batch_number(self):
        """
        Genera un número de lote en el formato SKU-YYMMDD-XXX.
        """
        # Obtén la fecha actual en el formato YYMMDD
        date_str = datetime.now().strftime('%y%m%d')
        
        # Obtén el número más alto actual para el SKU y la fecha
        max_batch = BatchNumber.objects.filter(sku=self.sku, batch_number__startswith=f"{self.sku.sku}-{date_str}").aggregate(models.Max('batch_number'))['batch_number__max']
        
        # Incrementa el sufijo del número de lote
        if max_batch:
            max_suffix = int(max_batch.split('-')[-1])
            new_suffix = max_suffix + 1
        else:
            new_suffix = 1

        # Formatea el nuevo número de lote
        new_batch_number = f"{self.sku.sku}-{date_str}-{new_suffix:03d}"
        
        return new_batch_number
