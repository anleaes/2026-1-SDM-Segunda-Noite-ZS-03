from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'hospedes'

router = routers.SimpleRouter()
router.register('', views.HospedeViewSet, basename='hospedes')

urlpatterns = [
    path('', include(router.urls))
]
