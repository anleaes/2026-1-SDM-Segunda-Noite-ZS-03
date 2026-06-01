from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([AllowAny])
def cadastrar_usuario(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", "")

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

    return Response({"token": token.key}, status=status.HTTP_201_CREATED)
