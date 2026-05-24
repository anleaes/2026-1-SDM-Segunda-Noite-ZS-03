from rest_framework import viewsets
from .models import Usuarios
from .serializer import UsuariosSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
