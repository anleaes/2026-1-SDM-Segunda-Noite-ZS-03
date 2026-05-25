from .models import Anfitriao
from rest_framework import viewsets
from .serializer import AnfitriaoSerializer


class AnfitriaoViewSet(viewsets.ModelViewSet):
    queryset = Anfitriao.objects.all()
    serializer_class = AnfitriaoSerializer
