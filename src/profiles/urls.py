from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('auth/token', TokenObtainPairView.as_view()),
    path('auth/token/verify', TokenVerifyView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view()),
]