from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "hospedagens"

router = routers.DefaultRouter()
router.register("", views.HospedagemViewSet, basename="hospedagens")

urlpatterns = [
    path("lista/", views.hospedagens_lista, name="hospedagens_lista"),
    path("novo/", views.hospedagem_criar, name="hospedagem_criar"),
    path("editar/<int:id>/", views.hospedagem_editar, name="hospedagem_editar"),
    path("excluir/<int:id>/", views.hospedagem_excluir, name="hospedagem_excluir"),
    path("", include(router.urls)),
]
