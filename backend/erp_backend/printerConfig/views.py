from rest_framework import viewsets
from .models import PrinterConfig
from .serializers import PrinterSerializer

class PrinterConfigViewSet(viewsets.ModelViewSet):
    queryset = PrinterConfig.objects.all()
    serializer_class = PrinterSerializer
