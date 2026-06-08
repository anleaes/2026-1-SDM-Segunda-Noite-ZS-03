from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from usuarios.permissoes import EhAnfitriaoOuLeitura

from .forms import HospedagemForm
from .models import Hospedagem
from .serializer import HospedagemSerializer


def tipo_usuario(request):
    return request.session.get("tipo_usuario")


def usuario_eh_hospede(request):
    return tipo_usuario(request) == "hospede"


class HospedagemViewSet(viewsets.ModelViewSet):
    queryset = Hospedagem.objects.all().order_by("id")
    serializer_class = HospedagemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EhAnfitriaoOuLeitura]


def hospedagens_lista(request):
    hospedagens = (
        Hospedagem.objects
        .select_related("endereco")
        .prefetch_related("comodidades")
        .all()
        .order_by("id")
    )

    return render(
        request,
        "hospedagens/hospedagens_lista.html",
        {"hospedagens": hospedagens, "tipo_usuario": tipo_usuario(request)},
    )


def hospedagem_criar(request):
    if usuario_eh_hospede(request):
        messages.error(request, "Hospedes nao podem criar hospedagens.")
        return redirect("hospedagens:hospedagens_lista")

    if request.method == "POST":
        form = HospedagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hospedagem criada com sucesso.")
            return redirect("hospedagens:hospedagens_lista")
    else:
        form = HospedagemForm()

    return render(
        request,
        "hospedagens/hospedagem_form.html",
        {"form": form, "titulo": "Nova hospedagem"},
    )


def hospedagem_editar(request, id):
    if usuario_eh_hospede(request):
        messages.error(request, "Hospedes nao podem editar hospedagens.")
        return redirect("hospedagens:hospedagens_lista")

    hospedagem = get_object_or_404(Hospedagem, id=id)

    if request.method == "POST":
        form = HospedagemForm(request.POST, instance=hospedagem)
        if form.is_valid():
            form.save()
            messages.success(request, "Hospedagem atualizada com sucesso.")
            return redirect("hospedagens:hospedagens_lista")
    else:
        form = HospedagemForm(instance=hospedagem)

    return render(
        request,
        "hospedagens/hospedagem_form.html",
        {"form": form, "titulo": "Editar hospedagem"},
    )


def hospedagem_excluir(request, id):
    if usuario_eh_hospede(request):
        messages.error(request, "Hospedes nao podem excluir hospedagens.")
        return redirect("hospedagens:hospedagens_lista")

    hospedagem = get_object_or_404(Hospedagem, id=id)

    if request.method == "POST":
        hospedagem.delete()
        messages.success(request, "Hospedagem excluida com sucesso.")

    return redirect("hospedagens:hospedagens_lista")
