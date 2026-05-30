from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "anfitrioes"

router = routers.DefaultRouter()
router.register("", views.AnfitriaoViewSet, basename="anfitrioes")

urlpatterns = [
    path("", include(router.urls)),
]