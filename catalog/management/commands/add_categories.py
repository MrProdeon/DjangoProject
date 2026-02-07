from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category
from config.settings import BASE_DIR
import os


class Command(BaseCommand):

    help = "Add categories to the database"

    def handle(self, *args, **options):

        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Категории успешно удалены"))
        fixture_path = os.path.join(BASE_DIR,
                                    "catalog",
                                    "fixtures",
                                    "category_fixture.json")

        call_command("loaddata", fixture_path)
        self.stdout.write(self.style.SUCCESS("Фикстура успешно добавлена"))
        self.stdout.write(self.style.SUCCESS("Добавлены категории: "))
        result = Category.objects.all()
        for category in result:
            self.stdout.write(self.style.SUCCESS(f"{category}"))

