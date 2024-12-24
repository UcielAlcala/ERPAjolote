# erp_backend/inventories/serializers.py

from rest_framework import serializers
from .models import Warehouse, InventoryItem

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'