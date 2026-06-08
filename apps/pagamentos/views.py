from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from usuarios.permissoes import EhHospedeOuLeitura

from .forms import PagamentoForm
from .models import Pagamento
from .serializer import PagamentoSerializer


def tipo_usuario(request):
    return request.session.get("tipo_usuario")


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = (
        Pagamento.objects
        .select_related("reserva")
        .all()
        .order_by("id")
    )
    serializer_class = PagamentoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, EhHospedeOuLeitura]


def pagamentos_lista(request):
    pagamentos = (
        Pagamento.objects
        .select_related("reserva")
        .all()
        .order_by("id")
    )

    return render(
        request,
        "pagamentos/pagamentos_lista.html",
        {"pagamentos": pagamentos, "tipo_usuario": tipo_usuario(request)},
    )


def pagamento_criar(request):
    if request.method == "POST":
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pagamento criado com sucesso.")
            return redirect("pagamentos:pagamentos_lista")
    else:
        initial = {}
        reserva_id = request.GET.get("reserva")
        if reserva_id:
            initial["reserva"] = reserva_id
        form = PagamentoForm(initial=initial)

    return render(
        request,
        "pagamentos/pagamento_form.html",
        {"form": form, "titulo": "Novo pagamento"},
    )


def pagamento_editar(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)

    if request.method == "POST":
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            messages.success(request, "Pagamento atualizado com sucesso.")
            return redirect("pagamentos:pagamentos_lista")
    else:
        form = PagamentoForm(instance=pagamento)

    return render(
        request,
        "pagamentos/pagamento_form.html",
        {"form": form, "titulo": "Editar pagamento"},
    )


def pagamento_excluir(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)

    if request.method == "POST":
        pagamento.delete()
        messages.success(request, "Pagamento excluido com sucesso.")

    return redirect("pagamentos:pagamentos_lista")
