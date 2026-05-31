from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "hospedes"

router = routers.DefaultRouter()
router.register("", views.HospedeViewSet, basename="hospedes")

urlpatterns = [
    path("", include(router.urls))
]