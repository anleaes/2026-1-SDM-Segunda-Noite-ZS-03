from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "reservas"

router = routers.SimpleRouter()
router.register("reservas", views.ReservaViewSet, basename="reserva")

urlpatterns = [
    path("lista/", views.reservas_lista, name="reservas_lista"),
    path("novo/", views.reserva_criar, name="reserva_criar"),
    path("editar/<int:id>/", views.reserva_editar, name="reserva_editar"),
    path("excluir/<int:id>/", views.reserva_excluir, name="reserva_excluir"),
    path("", include(router.urls))
]
