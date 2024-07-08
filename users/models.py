from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Lesson, Course

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

class Payment(models.Model):
    payer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="плательщик",
        **NULLABLE)
    date_payment = models.DateTimeField(
        auto_now_add=True, **NULLABLE,
        verbose_name='дата создания')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        **NULLABLE)
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        **NULLABLE)
    amount_paid = models.FloatField(
        verbose_name="сумма оплаты",
        null=True)
    transfer_method = models.CharField(
        max_length=50, **NULLABLE, verbose_name="способ оплаты")

    def __str__(self):
        return f"{self.user} - {self.paid_lesson if self.paid_lesson else self.paid_course}: {self.amount}"
    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"