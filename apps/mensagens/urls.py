from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "mensagens"

router = routers.DefaultRouter()
router.register("mensagens", views.MensagemViewSet, basename="mensagens")

urlpatterns = [
    path("lista/", views.mensagens_lista, name="mensagens_lista"),
    path("novo/", views.mensagem_criar, name="mensagem_criar"),
    path("editar/<int:id>/", views.mensagem_editar, name="mensagem_editar"),
    path("excluir/<int:id>/", views.mensagem_excluir, name="mensagem_excluir"),
    path("", include(router.urls)),
]
