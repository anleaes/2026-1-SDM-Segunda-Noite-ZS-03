from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "enderecos"

router = routers.DefaultRouter()
router.register("", views.EnderecoViewSet, basename="enderecos")

urlpatterns = [
    path("lista/", views.enderecos_lista, name="enderecos_lista"),
    path("novo/", views.endereco_criar, name="endereco_criar"),
    path("editar/<int:id>/", views.endereco_editar, name="endereco_editar"),
    path("excluir/<int:id>/", views.endereco_excluir, name="endereco_excluir"),
    path("", include(router.urls)),
]
