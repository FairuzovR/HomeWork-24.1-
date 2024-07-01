# Generated by Django 5.0.6 on 2024-07-01 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Сourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название курса"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=10000,
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="materials/photo",
                        verbose_name="картинка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название урока"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=10000,
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="materials/photo",
                        verbose_name="картинка",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        db_index=True,
                        max_length=128,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="lessons",
                        to="materials.сourse",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
