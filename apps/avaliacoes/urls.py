from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "avaliacoes"

router = routers.DefaultRouter()
router.register("", views.AvaliacaoViewSet, basename="avaliacoes")

urlpatterns = [
    path("", include(router.urls)),
]