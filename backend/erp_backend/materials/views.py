# erp_backend/materials/views.py

from rest_framework import viewsets
from .models import Material
from .serializers import MaterialSerializer
from .filters import MaterialFilter
from django_filters.rest_framework import DjangoFilterBackend

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MaterialFilter
