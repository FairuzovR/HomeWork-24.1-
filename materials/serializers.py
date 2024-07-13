from rest_framework import serializers
from materials.validators import validate_urls
from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validate_urls])
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)

    def get_count_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ("id", "title", "description", "image", "count_lessons", "lessons")
