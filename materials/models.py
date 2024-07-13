from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(
        max_length=10000, verbose_name="Описание курса", **NULLABLE
    )
    image = models.ImageField(
        upload_to="materials/photo", verbose_name="картинка", **NULLABLE
    )
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name="владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    description = models.TextField(
        max_length=10000, verbose_name="Описание урока", **NULLABLE
    )
    image = models.ImageField(
        upload_to="materials/photo", verbose_name="картинка", **NULLABLE
    )
    url = models.URLField(max_length=128, db_index=True, unique=True, **NULLABLE)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        related_name="lessons",
        **NULLABLE
    )
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name="владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class Subscription(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name="подписчики")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")
    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
