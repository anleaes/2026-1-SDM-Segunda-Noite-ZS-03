from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "mensagens"

router = routers.SimpleRouter()
router.register("", views.MensagemViewSet, basename="mensagens")

urlpatterns = [
    path("", include(router.urls))
]