# erp_backend/inventory_transaction/serializers.py

from rest_framework import serializers
from .models import InventoryTransaction

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = '__all__'
