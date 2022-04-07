from django.urls import path, include
from .views import ServiceViewSet, PlanViewSet, RechargeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'service',ServiceViewSet)
router.register(r'plan', PlanViewSet)
router.register(r'recharge', RechargeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
