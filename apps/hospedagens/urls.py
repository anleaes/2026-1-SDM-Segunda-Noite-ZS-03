from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "hospedagens"

router = routers.DefaultRouter()
router.register("", views.HospedagemViewSet, basename="hospedagens")

urlpatterns = [
    path("", include(router.urls)),
]