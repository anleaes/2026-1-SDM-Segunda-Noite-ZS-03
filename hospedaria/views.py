from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from hospedes.models import Hospede


def obter_ou_criar_hospede(usuario):
    email = usuario.email or f"{usuario.username}@email.local"
    hospede = Hospede.objects.filter(email=email).first()

    if hospede:
        return hospede

    return Hospede.objects.create(
        nome=usuario.username,
        email=email,
        telefone="Nao informado",
        documento=f"user-{usuario.id}",
        nacionalidade="Nao informada",
        data_nascimento="2000-01-01",
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def cadastrar_usuario(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")
    tipo_login = request.data.get("tipo_login")

    if not username or not password:
        return Response(
            {"erro": "Informe usuario e senha."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"erro": "Este usuario ja existe."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    usuario = User.objects.create_user(
        username=username,
        password=password,
        email=email,
    )
    token, _ = Token.objects.get_or_create(user=usuario)

    if tipo_login == "hospede":
        obter_ou_criar_hospede(usuario)

    return Response({"token": token.key}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil_hospede(request):
    hospede = obter_ou_criar_hospede(request.user)
    return Response({"id": hospede.id})
