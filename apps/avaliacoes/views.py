from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import AvaliacaoForm
from .models import Avaliacao
from .serializer import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all().order_by("id")
    serializer_class = AvaliacaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


def avaliacoes_lista(request):
    avaliacoes = (
        Avaliacao.objects
        .select_related("hospedagem")
        .all()
        .order_by("id")
    )

    return render(
        request,
        "avaliacoes/avaliacoes_lista.html",
        {"avaliacoes": avaliacoes},
    )


def avaliacao_criar(request):
    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Avaliacao criada com sucesso.")
            return redirect("avaliacoes:avaliacoes_lista")
    else:
        form = AvaliacaoForm()

    return render(
        request,
        "avaliacoes/avaliacao_form.html",
        {"form": form, "titulo": "Nova avaliacao"},
    )


def avaliacao_editar(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)

    if request.method == "POST":
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            messages.success(request, "Avaliacao atualizada com sucesso.")
            return redirect("avaliacoes:avaliacoes_lista")
    else:
        form = AvaliacaoForm(instance=avaliacao)

    return render(
        request,
        "avaliacoes/avaliacao_form.html",
        {"form": form, "titulo": "Editar avaliacao"},
    )


def avaliacao_excluir(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)

    if request.method == "POST":
        avaliacao.delete()
        messages.success(request, "Avaliacao excluida com sucesso.")

    return redirect("avaliacoes:avaliacoes_lista")
