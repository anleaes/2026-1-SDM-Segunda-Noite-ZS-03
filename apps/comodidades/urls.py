from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'comodidades'

router = routers.DefaultRouter()
router.register('', views.ComodidadeViewSet, basename='comodidades')

urlpatterns = [
    path('', include(router.urls)),
]
