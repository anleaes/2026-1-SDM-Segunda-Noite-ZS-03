from .models import Mensagem
from rest_framework import viewsets
from .serializer import MensagemSerializer


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
