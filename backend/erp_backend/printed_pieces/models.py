# erp_backend/printed_pieces/models.py

from django.db import models
from erp_backend.materials.models import Material
from erp_backend.sku.models import generate_sku

class PrintedPiece(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    print_time = models.IntegerField()  # Ahora es un campo de tipo entero que representa minutos
    cost = models.FloatField(default=0.0)  # Valor por defecto para cost
    sku = models.CharField(max_length=10, unique=True, blank=True)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def calculate_cost(self):
        total_cost = 0.0
        for material in self.materials.all():
            material_cost = material.material.cost_per_unit
            if material.unit == 'kg':
                total_cost += material_cost * (material.quantity * 1000)
            else:  # Assuming 'g' or other units are handled similarly
                total_cost += material_cost * material.quantity
        self.cost = total_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = generate_sku('PI')
        super().save(*args, **kwargs)
    
class PrintedPieceMaterial(models.Model):
    UNIT_CHOICES = [
        ('g', 'Gramos'),
        ('kg', 'Kilogramos'),
    ]
    
    id = models.AutoField(primary_key=True)
    printed_piece = models.ForeignKey(PrintedPiece, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantity = models.FloatField()  # cantidad de material utilizado
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)  # unidad de medida restringida a 'g' o 'kg'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.material.name} for {self.printed_piece.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.printed_piece.calculate_cost()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.printed_piece.calculate_cost()
