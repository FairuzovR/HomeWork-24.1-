from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(
        max_length=10000, verbose_name="Описание курса", **NULLABLE
    )
    image = models.ImageField(
        upload_to="materials/photo", verbose_name="картинка", **NULLABLE
    )

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
    url = models.URLField(
        max_length=128, db_index=True, unique=True, **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        related_name="lessons",
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
