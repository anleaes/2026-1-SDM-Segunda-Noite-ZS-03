from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "avaliacoes"

router = routers.DefaultRouter()
router.register("", views.AvaliacaoViewSet, basename="avaliacoes")

urlpatterns = [
    path("lista/", views.avaliacoes_lista, name="avaliacoes_lista"),
    path("novo/", views.avaliacao_criar, name="avaliacao_criar"),
    path("editar/<int:id>/", views.avaliacao_editar, name="avaliacao_editar"),
    path("excluir/<int:id>/", views.avaliacao_excluir, name="avaliacao_excluir"),
    path("", include(router.urls)),
]
