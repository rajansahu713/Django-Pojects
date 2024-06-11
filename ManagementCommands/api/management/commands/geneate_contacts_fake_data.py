from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from api.models import Contacts

class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Generate fake contacts for each user
        for user in User.objects.all():
            for _ in range(100):
                contact = Contacts(
                    user = user,
                    name = faker.name(),
                    phone = faker.unique.random_number(digits=10, fix_len=True),
                    email = faker.email(),
                    message = faker.text(10)
                    )
                contact.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))
