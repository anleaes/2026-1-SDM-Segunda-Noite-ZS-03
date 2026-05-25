from rest_framework import viewsets
from .models import Hospedagens
from .serializer import HospedagensSerializer

class HospedagensViewSet(viewsets.ModelViewSet):
    queryset = Hospedagens.objects.all()
    serializer_class = HospedagensSerializer
