from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'enderecos'

router = routers.SimpleRouter()
router.register('', views.EnderecoViewSet, basename='enderecos')

urlpatterns = [
    path('', include(router.urls))
]
