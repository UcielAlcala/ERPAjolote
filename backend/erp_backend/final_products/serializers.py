from rest_framework import serializers
from .models import FinalProduct
from erp_backend.bom_printed_pieces.serializers import BOMPrintedPieceSerializer

class FinalProductSerializer(serializers.ModelSerializer):
    bom = BOMPrintedPieceSerializer(many=True, read_only=True, source='bom_items')

    class Meta:
        model = FinalProduct
        fields = ['id', 'name', 'description', 'total_cost', 'bom', 'sku', 'image', 'created_at', 'updated_at']
        read_only_fields = ['total_cost']