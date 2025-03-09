from django.contrib import admin

# Register your models here.
from .models import PrinterConfig

admin.site.register(PrinterConfig)
