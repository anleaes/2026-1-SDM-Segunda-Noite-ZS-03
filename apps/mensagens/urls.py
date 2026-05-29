from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'mensagens'

router = routers.SimpleRouter()
router.register('', views.MensagemViewSet, basename='mensagens')

urlpatterns = [
    path('', include(router.urls))
]
