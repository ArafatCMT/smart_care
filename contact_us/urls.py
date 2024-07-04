from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ContactUsViewSet

router = DefaultRouter()

router.register('', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]