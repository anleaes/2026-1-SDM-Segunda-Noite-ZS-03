from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import ReservaForm
from .models import Reserva
from .serializer import ReservaSerializer


def tipo_usuario(request):
    return request.session.get("tipo_usuario")


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.select_related("hospedagem", "hospede").all().order_by("id")
    serializer_class = ReservaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


def reservas_lista(request):
    reservas = (
        Reserva.objects
        .select_related("hospedagem", "hospede")
        .all()
        .order_by("id")
    )

    return render(
        request,
        "reservas/reservas_lista.html",
        {"reservas": reservas, "tipo_usuario": tipo_usuario(request)},
    )


def reserva_criar(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva criada com sucesso.")
            return redirect("reservas:reservas_lista")
    else:
        initial = {}
        hospedagem_id = request.GET.get("hospedagem")
        if hospedagem_id:
            initial["hospedagem"] = hospedagem_id
        form = ReservaForm(initial=initial)

    return render(
        request,
        "reservas/reserva_form.html",
        {"form": form, "titulo": "Nova reserva"},
    )


def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva atualizada com sucesso.")
            return redirect("reservas:reservas_lista")
    else:
        form = ReservaForm(instance=reserva)

    return render(
        request,
        "reservas/reserva_form.html",
        {"form": form, "titulo": "Editar reserva"},
    )


def reserva_excluir(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == "POST":
        reserva.delete()
        messages.success(request, "Reserva excluida com sucesso.")

    return redirect("reservas:reservas_lista")
