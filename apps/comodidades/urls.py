from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'comodidades'

router = routers.SimpleRouter()
router.register('', views.ComodidadeViewSet, basename='comodidades')

urlpatterns = [
    path('', include(router.urls))
]
