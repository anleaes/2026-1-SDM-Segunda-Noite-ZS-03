from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Hospedagem
from .serializer import HospedagemSerializer

class HospedagemViewSet(viewsets.ModelViewSet):
    queryset = Hospedagem.objects.all()
    serializer_class = HospedagemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
