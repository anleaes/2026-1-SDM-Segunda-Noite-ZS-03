from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "reservas"

router = routers.SimpleRouter()
router.register("reservas", views.ReservaViewSet, basename="reserva")

urlpatterns = [
    path("", include(router.urls))
]