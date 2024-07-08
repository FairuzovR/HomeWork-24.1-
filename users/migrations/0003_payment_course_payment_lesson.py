# Generated by Django 5.0.6 on 2024-07-07 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
                verbose_name="оплаченный курс",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.lesson",
                verbose_name="оплаченный курс",
            ),
        ),
    ]
