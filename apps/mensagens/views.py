from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import MensagemForm
from .models import Mensagem
from .serializer import MensagemSerializer


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all().order_by("id")
    serializer_class = MensagemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


def mensagens_lista(request):
    mensagens = (
        Mensagem.objects
        .select_related("hospedagem")
        .all()
        .order_by("id")
    )

    return render(
        request,
        "mensagens/mensagens_lista.html",
        {"mensagens": mensagens},
    )


def mensagem_criar(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem criada com sucesso.")
            return redirect("mensagens:mensagens_lista")
    else:
        form = MensagemForm()

    return render(
        request,
        "mensagens/mensagem_form.html",
        {"form": form, "titulo": "Nova mensagem"},
    )


def mensagem_editar(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)

    if request.method == "POST":
        form = MensagemForm(request.POST, instance=mensagem)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem atualizada com sucesso.")
            return redirect("mensagens:mensagens_lista")
    else:
        form = MensagemForm(instance=mensagem)

    return render(
        request,
        "mensagens/mensagem_form.html",
        {"form": form, "titulo": "Editar mensagem"},
    )


def mensagem_excluir(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)

    if request.method == "POST":
        mensagem.delete()
        messages.success(request, "Mensagem excluida com sucesso.")

    return redirect("mensagens:mensagens_lista")
