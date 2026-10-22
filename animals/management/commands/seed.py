from datetime import date, timedelta

from django.core.management.base import BaseCommand

from animals.models import AdoptionApplication, Animal


class Command(BaseCommand):
    help = "Replace every animal with three animals and two adoption applications."

    def handle(self, *args, **options):
        # Deleting the animals also deletes their applications, so the command
        # can run again.
        Animal.objects.all().delete()

        peanut = Animal.objects.create(
            name="Peanut",
            species=Animal.Species.CAT,
            birth_date=date.today() - timedelta(days=60),
        )
        Animal.objects.create(
            name="Rocket",
            species=Animal.Species.DOG,
            breed="Beagle mix",
            birth_date=date.today() - timedelta(days=3 * 365),
        )
        Animal.objects.create(
            name="Smokey",
            species=Animal.Species.CAT,
            birth_date=date.today() - timedelta(days=4 * 365),
            status=Animal.Status.PENDING,
        )

        AdoptionApplication.objects.create(
            animal=peanut, applicant_name="Maria", email="maria@example.com"
        )
        AdoptionApplication.objects.create(
            animal=peanut, applicant_name="Aisha", email="aisha@example.com"
        )

        self.stdout.write("Created 3 animals and 2 adoption applications.")
