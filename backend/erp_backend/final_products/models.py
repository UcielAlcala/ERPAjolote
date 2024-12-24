from django.db import models
from erp_backend.sku.models import generate_sku

class FinalProduct(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=10, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_cost = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = generate_sku('PF')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
