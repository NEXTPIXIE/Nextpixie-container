from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from user_account.models import UserOtp



class Command(BaseCommand):
    help = 'Delete residual otps from the database'


    def handle(self, *args, **options):
        
        otps = UserOtp.objects.all()
        otps.delete()

        self.stdout.write(self.style.SUCCESS("Successfully deleted residual otps from the db."))