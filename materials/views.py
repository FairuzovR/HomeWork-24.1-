from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscription
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from materials.paginators import StudyPagination
from users.permissions import IsModerator, IsUser

from django.shortcuts import get_object_or_404


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StudyPagination

    def get_permissions(self):
        if self.action == "create":
            self.permissions = (~IsModerator)
        if self.action == "destroy":
            self.permissions = (~IsModerator | IsUser)
        if self.action in ["update", "retriew", "patrial_update", "list"]:
            self.permissions = (IsModerator | IsUser)
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_queryset(self):
        if IsModerator().has_permission(self.request, self):
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=self.request.user)


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = StudyPagination
    permission_classes = [IsModerator | IsUser]

    def get_queryset(self):
        if IsModerator().has_permission(self.request, self):
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsUser]


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsUser]


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator | IsUser]

class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subscription, created = Subscription.objects.get_or_create(user=user, course=course_item)
        if not created:
            subscription.delete()
            messages = "подписка удалена"
        else:
            messages = "подписка оформлена"

        return Response({'messages': messages})
