# erp_backend/sku/serializers.py

from rest_framework import serializers
from .models import SKU

class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'
