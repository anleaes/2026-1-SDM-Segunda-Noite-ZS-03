from .models import Hospedagem
from rest_framework import viewsets
from .serializer import HospedagemSerializer


class HospedagemViewSet(viewsets.ModelViewSet):
    queryset = Hospedagem.objects.all()
    serializer_class = HospedagemSerializer
