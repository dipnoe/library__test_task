from django.core.management import BaseCommand

from src.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = 'admin@admin.com'
        password = '123qwe456rty'

        user = User.objects.create(
            email=email,
            first_name='Admin',
            last_name='Admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password(password)
        user.save()
        print("Superuser is created successfully.\n"
              "Don't forget to change password.\n\n"
              f"Email: '{email}'\n"
              f"Password: '{password}'")
