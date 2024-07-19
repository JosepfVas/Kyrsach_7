from django.urls import path
from rest_framework.permissions import AllowAny
from users.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserDeleteAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("list/", UserListAPIView.as_view(), name="user_list"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("retrieve/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("delete/", UserDeleteAPIView.as_view(), name="user_delete"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
