from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import MensagemForm, RespostaMensagemForm
from .models import Mensagem
from .serializer import MensagemSerializer


def tipo_usuario(request):
    return request.session.get("tipo_usuario")


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
        {"mensagens": mensagens, "tipo_usuario": tipo_usuario(request)},
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


def mensagem_responder(request, id):
    mensagem = get_object_or_404(Mensagem, id=id)

    if request.method == "POST":
        form = RespostaMensagemForm(request.POST, instance=mensagem)
        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.lida = True
            resposta.respondida_em = timezone.now()
            resposta.save()
            messages.success(request, "Mensagem respondida com sucesso.")
            return redirect("mensagens:mensagens_lista")
    else:
        form = RespostaMensagemForm(instance=mensagem)

    return render(
        request,
        "mensagens/mensagem_responder.html",
        {"form": form, "mensagem": mensagem, "titulo": "Responder mensagem"},
    )
