from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import EnderecoForm
from .models import Endereco
from .serializer import EnderecoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all().order_by("id")
    serializer_class = EnderecoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


def enderecos_lista(request):
    enderecos = Endereco.objects.all().order_by("id")

    return render(
        request,
        "enderecos/enderecos_lista.html",
        {"enderecos": enderecos},
    )


def endereco_criar(request):
    if request.method == "POST":
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Endereco criado com sucesso.")
            return redirect("enderecos:enderecos_lista")
    else:
        form = EnderecoForm()

    return render(
        request,
        "enderecos/endereco_form.html",
        {"form": form, "titulo": "Novo endereco"},
    )


def endereco_editar(request, id):
    endereco = get_object_or_404(Endereco, id=id)

    if request.method == "POST":
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            messages.success(request, "Endereco atualizado com sucesso.")
            return redirect("enderecos:enderecos_lista")
    else:
        form = EnderecoForm(instance=endereco)

    return render(
        request,
        "enderecos/endereco_form.html",
        {"form": form, "titulo": "Editar endereco"},
    )


def endereco_excluir(request, id):
    endereco = get_object_or_404(Endereco, id=id)

    if request.method == "POST":
        endereco.delete()
        messages.success(request, "Endereco excluido com sucesso.")

    return redirect("enderecos:enderecos_lista")
