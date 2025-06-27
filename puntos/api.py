
from rest_framework import viewsets
from .models import Punto
from .serializers import PuntoSerializer

class PuntoViewSet(viewsets.ModelViewSet):
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer
