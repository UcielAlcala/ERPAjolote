from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem, Supplier

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'purchase_order', 'material', 'quantity', 'cost_per_unit', 'total_cost', 'received_quantity', 'created_at', 'updated_at']
        read_only_fields = ['total_cost', 'created_at', 'updated_at']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True, required=False)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'supplier', 'order_date', 'expected_date', 'status', 'total_cost', 'items', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items', None)
        purchase_order = PurchaseOrder.objects.create(**validated_data)
        if items_data:
            for item_data in items_data:
                PurchaseOrderItem.objects.create(purchase_order=purchase_order, **item_data)
        return purchase_order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.expected_date = validated_data.get('expected_date', instance.expected_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if items_data is not None:
            # Mantiene un registro de los ítems existentes que se deben actualizar
            existing_items = {item.id: item for item in instance.items.all()}
            
            for item_data in items_data:
                item_id = item_data.get('id', None)
                if item_id and item_id in existing_items:
                    # Si el ítem ya existe, se actualiza
                    item = existing_items.pop(item_id)
                    item.material = item_data.get('material', item.material)
                    item.quantity = item_data.get('quantity', item.quantity)
                    item.cost_per_unit = item_data.get('cost_per_unit', item.cost_per_unit)
                    item.total_cost = item_data.get('total_cost', item.total_cost)
                    item.received_quantity = item_data.get('received_quantity', item.received_quantity)
                    item.save()
                else:
                    # Si el ítem no existe, se crea uno nuevo
                    PurchaseOrderItem.objects.create(purchase_order=instance, **item_data)
            
            # Elimina los ítems que ya no están presentes en los datos actualizados
            for item in existing_items.values():
                item.delete()

        return instance
