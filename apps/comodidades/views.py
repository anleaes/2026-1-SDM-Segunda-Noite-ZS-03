from .models import Comodidade
from rest_framework import viewsets
from .serializer import ComodidadeSerializer


class ComodidadeViewSet(viewsets.ModelViewSet):
    queryset = Comodidade.objects.all()
    serializer_class = ComodidadeSerializer
