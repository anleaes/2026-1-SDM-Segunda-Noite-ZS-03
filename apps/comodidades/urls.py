from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "comodidades"

router = routers.DefaultRouter()
router.register("", views.ComodidadeViewSet, basename="comodidades")

urlpatterns = [
    path("lista/", views.comodidades_lista, name="comodidades_lista"),
    path("novo/", views.comodidade_criar, name="comodidade_criar"),
    path("editar/<int:id>/", views.comodidade_editar, name="comodidade_editar"),
    path("excluir/<int:id>/", views.comodidade_excluir, name="comodidade_excluir"),
    path("", include(router.urls)),
]
