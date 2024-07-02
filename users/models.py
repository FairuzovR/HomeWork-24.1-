from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почтв", help_text="Укажите почту"
    )
    city = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Страна", help_text="Введите страну"
    )
    avatar = models.ImageField(
        upload_to="users/photo/",
        verbose_name="Аватар",
        **NULLABLE,
        help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
