# erp_backend/materials/models.py

from django.db import models
from erp_backend.sku.models import generate_sku

class Material(models.Model):
    TYPE_CHOICES = [
        ('Producción', 'Producción'),
        ('Empaque', 'Empaque'),
        ('Envío', 'Envío')
    ]

    SUB_TYPE_CHOICES = [
        ('Filamento', 'Filamento'),
        ('Insumos', 'Insumos'),
        ('Refacciones', 'Refacciones'),
        ('Pegamento', 'Pegamento')
    ]

    UNIT_CHOICES = [
        ('g', 'Gramos'),
        ('kg', 'Kilogramos'),
        ('pz', 'Piezas')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    sub_type = models.CharField(max_length=50, choices=SUB_TYPE_CHOICES)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)  # e.g., g, ml, m, unidades
    cost_per_unit = models.FloatField()
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=10, unique=True, blank=True)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = generate_sku('MP')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
