# erp_backend/inventories/views.py

from rest_framework import viewsets
from .models import Warehouse, InventoryItem
from .serializers import WarehouseSerializer, InventoryItemSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer