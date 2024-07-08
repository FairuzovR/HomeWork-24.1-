from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserListAPIView

app_name = UsersConfig.name
# router = SimpleRouter()
# router.register("", CourseViewSet)

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payment_list"),
    path("", UserListAPIView.as_view(), name="user_list"),
]
