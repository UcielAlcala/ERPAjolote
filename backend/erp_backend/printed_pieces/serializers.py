# erp_backend/printed_pieces/serializers.py

from rest_framework import serializers
from .models import PrintedPiece, PrintedPieceMaterial
from erp_backend.materials.serializers import MaterialSerializer
from erp_backend.materials.models import Material

class PrintedPieceMaterialSerializer(serializers.ModelSerializer):
    material = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())
    printed_piece = serializers.PrimaryKeyRelatedField(queryset=PrintedPiece.objects.all())

    class Meta:
        model = PrintedPieceMaterial
        fields = ['id', 'printed_piece', 'material', 'quantity', 'unit', 'created_at', 'updated_at']

class PrintedPieceSerializer(serializers.ModelSerializer):
    materials = PrintedPieceMaterialSerializer(many=True, required=False)

    class Meta:
        model = PrintedPiece
        fields = ['id', 'name', 'print_time', 'cost', 'materials', 'sku', 'image']

    def create(self, validated_data):
        materials_data = validated_data.pop('materials', None)
        image = validated_data.pop('image', None)
        printed_piece = PrintedPiece.objects.create(**validated_data)

        if image:
            printed_piece.image = image
            printed_piece.save()

        if materials_data:
            for material_data in materials_data:
                PrintedPieceMaterial.objects.create(printed_piece=printed_piece, **material_data)
        return printed_piece

    def update(self, instance, validated_data):
        materials_data = validated_data.pop('materials', None)
        image = validated_data.pop('image', None)
        if image:
            instance.image = image
        
        instance.name = validated_data.get('name', instance.name)
        instance.print_time = validated_data.get('print_time', instance.print_time)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.save()

        if materials_data is not None:
            instance.materials.all().delete()
            for material_data in materials_data:
                PrintedPieceMaterial.objects.create(printed_piece=instance, **material_data)

        return instance
