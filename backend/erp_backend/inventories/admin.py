# erp_backend/inventories/admin.py

from django.contrib import admin
from .models import Warehouse, InventoryItem

admin.site.register(Warehouse)
admin.site.register(InventoryItem)
