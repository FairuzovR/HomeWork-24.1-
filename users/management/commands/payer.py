from django.core.management import BaseCommand
from users.models import Payment

class Command(BaseCommand):

    def handle(self, *args, **options):
        user_list = [
            {'payer_id': 2, 'course_id': 3, 'amount_paid': '70000', 'transfer_method': 'безналичный'},
            {'payer_id': 1, 'lesson_id': 2, 'amount_paid': '1500', 'transfer_method': 'безналичный'},
            {'payer_id': 1, 'lesson_id': 3, 'amount_paid': '150000', 'transfer_method': 'наличный'}
        ]

        for user_data in user_list:
            Payment.objects.create(**user_data)