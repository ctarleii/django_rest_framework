from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from accounts.views import SignUpView, LoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("login/", LoginView.as_view(), name="login"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]