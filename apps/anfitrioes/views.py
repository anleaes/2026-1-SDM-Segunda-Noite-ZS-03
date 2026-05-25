from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Anfitriao
from .serializer import AnfitriaoSerializer

class AnfitriaoViewSet(viewsets.ModelViewSet):
    queryset = Anfitriao.objects.all()
    serializer_class = AnfitriaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
