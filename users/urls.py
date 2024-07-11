from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserListAPIView, UserCreateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name
# router = SimpleRouter()
# router.register("", CourseViewSet)

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name="payment_list"),

    path('', UserListAPIView.as_view(), name="user_list"),
    path('register/',UserCreateAPIView.as_view(), name="register"),

    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

