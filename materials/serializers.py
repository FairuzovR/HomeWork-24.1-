from rest_framework import serializers
from materials.validators import validate_urls
from materials.models import Course, Lesson, Subscription


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validate_urls])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)
    subscription = serializers.SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lessons.count()

    def get_subscription(self, obj):
        request = self.context.get("request")
        user = None
        if request:
            user = request.user
        return obj.subscription_set.filter(user=user).exists()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "description",
            "image",
            "count_lessons",
            "lessons",
            "subscription",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
