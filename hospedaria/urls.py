"""
URL configuration for hospedaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
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
