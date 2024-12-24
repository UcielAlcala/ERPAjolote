from django.db import models

class SKU(models.Model):
    CATEGORY_CHOICES = [
        ('MP', 'Material Crudo'),
        ('PI', 'Pieza Impresa'),
        ('PF', 'Producto Final'),
    ]
    
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    code = models.PositiveIntegerField(blank=True)
    sku = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku

def generate_sku(category):
    """
    Genera y registra un SKU basado en la categoría proporcionada.
    
    :param category: La categoría del producto (p. ej., "MP", "PI", "PF").
    :return: Un nuevo SKU único.
    """
    # Obtiene el código más alto actual para la categoría
    max_code = SKU.objects.filter(category=category).aggregate(models.Max('code'))['code__max'] or 0
    new_code = max_code + 1
    
    # Genera el nuevo SKU
    new_sku = f"{category}{new_code:05d}"
    
    # Registra el nuevo SKU en la base de datos
    SKU.objects.create(category=category, code=new_code, sku=new_sku)
    
    return new_sku