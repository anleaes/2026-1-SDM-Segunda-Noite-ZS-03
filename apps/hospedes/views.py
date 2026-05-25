from .models import Hospede
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import HospedeSerializer


class HospedeViewSet(viewsets.ModelViewSet):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
