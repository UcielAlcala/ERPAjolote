# erp_backend/batch_number/serializers.py

from rest_framework import serializers
from .models import BatchNumber

class BatchNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchNumber
        fields = '__all__'
