from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'anfitrioes'

router = routers.SimpleRouter()
router.register('', views.AnfitriaoViewSet, basename='anfitrioes')

urlpatterns = [
    path('', include(router.urls))
]
