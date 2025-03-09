from rest_framework import serializers
from .models import PrinterConfig

class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterConfig
        fields = '__all__'
