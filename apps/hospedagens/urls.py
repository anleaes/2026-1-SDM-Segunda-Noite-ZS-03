from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'hospedagens'

router = routers.DefaultRouter()
router.register('', views.HospedagemViewSet, basename='hospedagens')

urlpatterns = [
    path('', include(router.urls))
]
