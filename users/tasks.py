from celery import shared_task
from dateutil.relativedelta import relativedelta

from django.utils import timezone

from users.models import User

@shared_task
def chelast_login():
    users = User.objects.all()
    data_now = timezone.now()
    for user in users:
        if user.last_login:
            if user.last_login < (data_now - relativedelta(months=1)):
                user.is_active = False
                user.save()
        else:
            user.last_login = data_now
            user.save()