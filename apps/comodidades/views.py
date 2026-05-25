from rest_framework import viewsets
from .models import Comodidades
from .serializer import ComodidadesSerializer

class ComodidadesViewSet(viewsets.ModelViewSet):
    queryset = Comodidades.objects.all()
    serializer_class = ComodidadesSerializer
