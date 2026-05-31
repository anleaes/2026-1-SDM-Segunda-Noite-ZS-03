from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "pagamentos"

router = routers.SimpleRouter()
router.register("", views.PagamentoViewSet, basename="pagamentos")

urlpatterns = [
    path("", include(router.urls))
]

