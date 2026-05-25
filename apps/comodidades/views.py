from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Comodidade
from .serializer import ComodidadeSerializer

class ComodidadeViewSet(viewsets.ModelViewSet):
    queryset = Comodidade.objects.all()
    serializer_class = ComodidadeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
