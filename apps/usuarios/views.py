from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from anfitrioes.models import Anfitriao
from hospedes.models import Hospede
from .forms import CadastroForm, LoginForm
from .models import Usuario
from .serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(ativo=True).order_by("id")
    serializer_class = UsuarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


def login_usuario(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            tipo_usuario = form.cleaned_data["tipo_usuario"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                request.session["tipo_usuario"] = tipo_usuario
                return redirect("home")

            messages.error(request, "Usuario ou senha invalidos.")
    else:
        form = LoginForm()

    return render(request, "usuarios/login.html", {"form": form})


def cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            cpf = form.cleaned_data["cpf"]

            if User.objects.filter(username=username).exists():
                form.add_error("username", "Este usuario ja existe.")
            elif Usuario.objects.filter(email=email).exists():
                form.add_error("email", "Este email ja esta cadastrado.")
            elif Usuario.objects.filter(cpf=cpf).exists():
                form.add_error("cpf", "Este CPF ja esta cadastrado.")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=form.cleaned_data["password"],
                    email=email,
                )
                Usuario.objects.create(
                    nome=form.cleaned_data["nome"],
                    email=email,
                    telefone=form.cleaned_data["telefone"],
                    cpf=cpf,
                    data_nascimento=form.cleaned_data["data_nascimento"],
                )

                if form.cleaned_data["tipo_usuario"] == "anfitriao":
                    Anfitriao.objects.create(
                        nome=form.cleaned_data["nome"],
                        email=email,
                        telefone=form.cleaned_data["telefone"],
                        documento=form.cleaned_data["documento"],
                        bio=form.cleaned_data["bio"],
                    )
                else:
                    Hospede.objects.create(
                        nome=form.cleaned_data["nome"],
                        email=email,
                        telefone=form.cleaned_data["telefone"],
                        documento=form.cleaned_data["documento"],
                        nacionalidade=form.cleaned_data["nacionalidade"] or "Nao informada",
                        data_nascimento=form.cleaned_data["data_nascimento"],
                    )

                login(request, user)
                request.session["tipo_usuario"] = form.cleaned_data["tipo_usuario"]
                messages.success(request, "Cadastro criado com sucesso.")
                return redirect("home")
    else:
        form = CadastroForm()

    return render(request, "usuarios/cadastro.html", {"form": form})


def logout_usuario(request):
    logout(request)
    return redirect("usuarios:login_usuario")
