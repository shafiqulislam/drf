from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'members', MemberViewSet, basename='member')

urlpatterns = [
    # JWT endpoints
    path('v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Protected APIs
    path('v1/', include(router.urls)),
]