from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from usuarios.permissoes import EhAnfitriaoOuLeitura

from .forms import ComodidadeForm
from .models import Comodidade
from .serializer import ComodidadeSerializer


class ComodidadeViewSet(viewsets.ModelViewSet):
    queryset = Comodidade.objects.all().order_by("id")
    serializer_class = ComodidadeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EhAnfitriaoOuLeitura]


def comodidades_lista(request):
    comodidades = Comodidade.objects.all().order_by("id")

    return render(
        request,
        "comodidades/comodidades_lista.html",
        {"comodidades": comodidades},
    )


def comodidade_criar(request):
    if request.method == "POST":
        form = ComodidadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comodidade criada com sucesso.")
            return redirect("comodidades:comodidades_lista")
    else:
        form = ComodidadeForm()

    return render(
        request,
        "comodidades/comodidade_form.html",
        {"form": form, "titulo": "Nova comodidade"},
    )


def comodidade_editar(request, id):
    comodidade = get_object_or_404(Comodidade, id=id)

    if request.method == "POST":
        form = ComodidadeForm(request.POST, instance=comodidade)
        if form.is_valid():
            form.save()
            messages.success(request, "Comodidade atualizada com sucesso.")
            return redirect("comodidades:comodidades_lista")
    else:
        form = ComodidadeForm(instance=comodidade)

    return render(
        request,
        "comodidades/comodidade_form.html",
        {"form": form, "titulo": "Editar comodidade"},
    )


def comodidade_excluir(request, id):
    comodidade = get_object_or_404(Comodidade, id=id)

    if request.method == "POST":
        comodidade.delete()
        messages.success(request, "Comodidade excluida com sucesso.")

    return redirect("comodidades:comodidades_lista")
