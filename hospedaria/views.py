from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from usuarios.auth_perfil import (
    TIPOS_LOGIN,
    perfil_login,
    perfil_por_tipo,
)


def home(request):
    return render(request, "home.html")


@api_view(["POST"])
@permission_classes([AllowAny])
def cadastrar_usuario(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")
    tipo_login = request.data.get("tipo_login")

    if not username or not password or not tipo_login:
        return Response(
            {"erro": "Informe usuario, senha e tipo de login."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if tipo_login not in TIPOS_LOGIN:
        return Response(
            {"erro": "Tipo de login invalido."},
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
    perfil = perfil_por_tipo(usuario, tipo_login)

    return Response(
        {"token": token.key, **perfil},
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil_hospede(request):
    perfil = perfil_por_tipo(request.user, "hospede")
    return Response({"id": perfil["hospede_id"]})


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil_login_usuario(request):
    return Response(perfil_login(request.user))
