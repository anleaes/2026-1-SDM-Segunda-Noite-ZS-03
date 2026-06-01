from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "usuarios"

router = routers.SimpleRouter()
router.register("usuarios", views.UsuarioViewSet, basename="usuario")

urlpatterns = [
    path("login/", views.login_usuario, name="login_usuario"),
    path("cadastro/", views.cadastro_usuario, name="cadastro_usuario"),
    path("perfil/", views.perfil_usuario, name="perfil_usuario"),
    path("logout/", views.logout_usuario, name="logout_usuario"),
    path("", include(router.urls))
]
