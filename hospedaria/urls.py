from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-autenticacao/', obtain_auth_token),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('enderecos/', include('enderecos.urls', namespace='enderecos')),
    path('comodidades/', include('comodidades.urls', namespace='comodidades')),
    path('hospedes/', include('hospedes.urls', namespace='hospedes')),
    path('anfitrioes/', include('anfitrioes.urls', namespace='anfitrioes')),
    path('hospedagens/', include('hospedagens.urls', namespace='hospedagens')),
    path('reservas/', include('reservas.urls', namespace='reservas')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
    path('avaliacoes/', include('avaliacoes.urls', namespace='avaliacoes')),
    path('mensagens/', include('mensagens.urls', namespace='mensagens')),
]
