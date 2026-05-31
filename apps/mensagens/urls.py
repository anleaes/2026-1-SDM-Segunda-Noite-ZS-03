from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "mensagens"

router = routers.DefaultRouter()
router.register("mensagens", views.MensagemViewSet, basename="mensagens")

urlpatterns = [
    path("", include(router.urls)),
]