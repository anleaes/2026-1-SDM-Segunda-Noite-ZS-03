from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "pagamentos"

router = routers.SimpleRouter()
router.register("pagamentos", views.PagamentoViewSet, basename="pagamento")

urlpatterns = [
    path("lista/", views.pagamentos_lista, name="pagamentos_lista"),
    path("novo/", views.pagamento_criar, name="pagamento_criar"),
    path("editar/<int:id>/", views.pagamento_editar, name="pagamento_editar"),
    path("excluir/<int:id>/", views.pagamento_excluir, name="pagamento_excluir"),
    path("", include(router.urls)),
]
