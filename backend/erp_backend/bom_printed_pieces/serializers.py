# erp_backend/bom_printed_pieces/serializers.py

from rest_framework import serializers
from .models import BOMPrintedPiece
from erp_backend.final_products.models import FinalProduct

class BOMPrintedPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMPrintedPiece
        fields = ['id', 'final_product', 'content_type', 'object_id', 'quantity', 'cost', 'created_at', 'updated_at']
        read_only_fields = ['cost']

    def create(self, validated_data):
        instance = super().create(validated_data)
        self.update_final_product_cost(instance.final_product)
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        self.update_final_product_cost(instance.final_product)
        return instance

    def delete(self, instance):
        final_product = instance.final_product
        instance.delete()
        self.update_final_product_cost(final_product)

    def update_final_product_cost(self, final_product):
        total_cost = sum(item.cost*item.quantity for item in final_product.bom_items.all())
        final_product.total_cost = total_cost
        final_product.save()