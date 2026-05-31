from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "usuarios"

router = routers.SimpleRouter()
router.register("usuarios", views.UsuarioViewSet, basename="usuario")

urlpatterns = [
    path("", include(router.urls))
]