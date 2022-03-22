from monTiGMagasin.models import DonneeHisto
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "update sales for each products based on quantity in stock"

    def handle(self, *args, **options):
        DonneeHisto.objects.all().delete()