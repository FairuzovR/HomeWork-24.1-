from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="fairuzov_renat@mail.ru")
        user.set_password("2162")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()