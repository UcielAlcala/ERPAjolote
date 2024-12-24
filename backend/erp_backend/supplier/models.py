from django.db import models
from django.core.exceptions import ValidationError

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField( blank=True, null=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        if not self.contact_email and not self.contact_phone:
            raise ValidationError('Debe proporcionar al menos un correo electrónico o un número de teléfono.')
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
