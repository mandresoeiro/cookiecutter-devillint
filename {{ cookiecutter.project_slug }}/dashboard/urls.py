from django.urls import path, include
from rest_framework import routers
from .views import DashboardHomeView, UserViewSet

app_name = "dashboard"

# Configuração do router para a API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Views regulares
    path("", DashboardHomeView.as_view(), name="home"),
    
    # API endpoints
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
