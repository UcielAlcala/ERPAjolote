# erp_backend/final_products/views.py
from rest_framework import viewsets
from .models import FinalProduct
from .serializers import FinalProductSerializer

class FinalProductViewSet(viewsets.ModelViewSet):
    queryset = FinalProduct.objects.all()
    serializer_class = FinalProductSerializer
