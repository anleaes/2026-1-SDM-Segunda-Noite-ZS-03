from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'hospedes'

router = routers.SimpleRouter()
router.register('', views.HospedeViewSet, basename='hospedes')

urlpatterns = [
    path('', include(router.urls))
]
