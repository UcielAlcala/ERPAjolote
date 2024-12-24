# erp_backend/printed_pieces/views.py

from rest_framework import viewsets
from .models import PrintedPiece, PrintedPieceMaterial
from .serializers import PrintedPieceSerializer, PrintedPieceMaterialSerializer

class PrintedPieceViewSet(viewsets.ModelViewSet):
    queryset = PrintedPiece.objects.all()
    serializer_class = PrintedPieceSerializer

class PrintedPieceMaterialViewSet(viewsets.ModelViewSet):
    queryset = PrintedPieceMaterial.objects.all()
    serializer_class = PrintedPieceMaterialSerializer
