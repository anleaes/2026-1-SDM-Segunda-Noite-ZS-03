from rest_framework.permissions import SAFE_METHODS, BasePermission

from .auth_perfil import TIPO_ANFITRIAO, TIPO_HOSPEDE, perfil_login


class PermiteLeituraPorPerfil(BasePermission):
    tipo_login = None

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return perfil_login(request.user)["tipo_login"] == self.tipo_login


class EhAnfitriaoOuLeitura(PermiteLeituraPorPerfil):
    tipo_login = TIPO_ANFITRIAO


class EhHospedeOuLeitura(PermiteLeituraPorPerfil):
    tipo_login = TIPO_HOSPEDE
