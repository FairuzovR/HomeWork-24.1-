# Generated by Django 5.0.6 on 2024-07-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payment_course_payment_lesson"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="amount_paid",
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ID сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="transfer_method",
            field=models.CharField(
                blank=True,
                default="card",
                max_length=50,
                null=True,
                verbose_name="способ оплаты",
            ),
        ),
    ]
