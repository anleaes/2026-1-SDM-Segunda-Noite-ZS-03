from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'enderecos'

router = routers.DefaultRouter()
router.register('', views.EnderecoViewSet, basename='enderecos')

urlpatterns = [
    path('', include(router.urls)),
]
