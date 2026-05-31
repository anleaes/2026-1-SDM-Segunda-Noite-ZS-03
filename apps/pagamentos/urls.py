Python
from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "pagamentos"

router = routers.SimpleRouter()
router.register("pagamentos", views.PagamentoViewSet, basename="pagamento")

urlpatterns = [
    path("", include(router.urls))
]