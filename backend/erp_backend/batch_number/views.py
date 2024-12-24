# erp_backend/batch_number/views.py

from rest_framework import viewsets
from .models import BatchNumber
from .serializers import BatchNumberSerializer

class BatchNumberViewSet(viewsets.ModelViewSet):
    queryset = BatchNumber.objects.all()
    serializer_class = BatchNumberSerializer
