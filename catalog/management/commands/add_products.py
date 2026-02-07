from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product
from config.settings import BASE_DIR
import os


class Command(BaseCommand):

    help = "Add products to the database"

    def handle(self, *args, **options):

        Product.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Продукты удалены."))
        fixture_path = os.path.join(BASE_DIR,
                                    "catalog",
                                    "fixtures",
                                    "product_fixture.json")

        call_command("loaddata", fixture_path)
        self.stdout.write(self.style.SUCCESS("Фикстура успешно добавлена"))
        self.stdout.write(self.style.SUCCESS("Добавлены продукты: "))
        result = Product.objects.all()
        for product in result:
            self.stdout.write(self.style.SUCCESS(f"{product}"))
