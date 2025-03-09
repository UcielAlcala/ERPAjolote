from django.db import models

class PrinterConfig(models.Model):
    PRINTER_TYPE_CHOICES = [
        ('P1P', 'P1P'),
        ('P1S', 'P1S'),
        ('A1 Mini', 'A1 Mini'),
    ]

    hostname = models.CharField(max_length=50, verbose_name="IP de la impresora")
    access_code = models.CharField(max_length=50, verbose_name="Código de acceso")
    serial_number = models.CharField(max_length=50, verbose_name="Número de serie")
    printer_name = models.CharField(max_length=100, verbose_name="Nombre de la impresora")
    printer_type = models.CharField(max_length=20, choices=PRINTER_TYPE_CHOICES, verbose_name="Tipo de impresora")

    def __str__(self):
        return f"{self.printer_name} ({self.hostname})"
