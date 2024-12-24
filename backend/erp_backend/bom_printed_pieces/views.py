# erp_backend/bom_printed_pieces/views.py
from rest_framework import viewsets
from .models import BOMPrintedPiece
from .serializers import BOMPrintedPieceSerializer

class BOMPrintedPieceViewSet(viewsets.ModelViewSet):
    queryset = BOMPrintedPiece.objects.all()
    serializer_class = BOMPrintedPieceSerializer
