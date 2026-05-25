from .models import Hospede
from rest_framework import viewsets
from .serializer import HospedeSerializer


class HospedeViewSet(viewsets.ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer
