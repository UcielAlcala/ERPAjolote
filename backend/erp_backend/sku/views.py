# erp_backend/sku/views.py

from rest_framework import viewsets
from .models import SKU
from .serializers import SKUSerializer

class SKUViewSet(viewsets.ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer
