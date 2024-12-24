# erp_backend/inventory_transaction/views.py

from rest_framework import viewsets
from .models import InventoryTransaction
from .serializers import InventoryTransactionSerializer

class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer
