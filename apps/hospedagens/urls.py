from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'hospedagens'

router = routers.SimpleRouter()
router.register('', views.HospedagemViewSet, basename='hospedagens')

urlpatterns = [
    path('', include(router.urls))
]
