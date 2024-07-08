from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        user_list = [
            {'email': 'farik@gmail.com'},
            {'email': 'farik1@gmail.com'},
        ]

        for user_data in user_list:
            User.objects.createuser(email=user_data['email'])