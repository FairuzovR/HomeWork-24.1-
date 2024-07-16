from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from materials.services import create_stripe_product, create_stripe_price, create_stripe_session
from materials.models import Course, Lesson


class PaymentListAPIView(ListAPIView):
    """
    List all payments made by users, with filters for lesson, course, and transfer method.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        "lesson",
        "course",
        "transfer_method",
    ]
    ordering_fields = [
        "date_payment",
    ]


class UserListAPIView(ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permissions = [AllowAny]

        return super().get_permissions()


class UserCreateAPIView(CreateAPIView):
    """
    Create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentCreateAPIView(CreateAPIView):
    """
    Payment create endpoint
    """
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.user = self.request.user

        course_id = self.request.data.get('course')
        lesson_id = self.request.data.get('lesson')
        if course_id:
            course_product = create_stripe_product(Course.objects.get(pk=course_id).title)
            course_price = create_stripe_price(instance.course.amount, course_product)
            session_id, payment_link = create_stripe_session(course_price)
        else:
            lesson_product = create_stripe_product(Lesson.objects.get(pk=lesson_id).title)
            lesson_price = create_stripe_price(instance.lesson.amount, lesson_product)
            session_id, payment_link = create_stripe_session(lesson_price)

        instance.session_id = session_id
        instance.payment_link = payment_link
        instance.save()