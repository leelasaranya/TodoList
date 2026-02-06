from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", register),   # ✅ THIS FIXES 404
]

