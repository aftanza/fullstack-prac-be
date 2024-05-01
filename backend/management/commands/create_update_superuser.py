from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Creates or updates a superuser"

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv(
            "ADMIN_USER"
        )  # You can make these configurable via command line or env vars
        email = os.getenv("ADMIN_EMAIL")  #
        password = os.getenv("ADMIN_PASSWORD")  #

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.email = email
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS("Successfully updated superuser."))
        else:
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Successfully created superuser."))
