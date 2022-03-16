from monTiGMagasin.models import InfoProduct
from django.core.management.base import BaseCommand
import time

class Command(BaseCommand):
    help = "update sales for each products based on quantity in stock"

    def handle(self, *args, **options):
        products = InfoProduct.objects.all()

        for product in products:
            if product.quantityInStock < 16 and product.sale:
                product.sale = False
                product.discount = 0.0
                product.percentage_reduc = 0

                product.save()

                self.stdout.write(self.style.SUCCESS(f"[{time.ctime()}] Removed sales for product id={product.tig_id}"))

                continue

            if 16 <= product.quantityInStock <= 64:
                product.sale = True
                product.discount = round(product.price *0.8, 2)
                product.percentage_reduc = 20

                product.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f"[{time.ctime()}] Successfully added sales product id={product.tig_id} price={product.price} qty={product.quantityInStock} discount={product.discount} percentage_reduc={product.percentage_reduc}"
                    )
                )

                continue

            if product.quantityInStock > 64:
                product.sale = True
                product.discount = round(product.price *0.5, 2)
                product.percentage_reduc = 50

                product.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f"[{time.ctime()}] Successfully added sales product id={product.tig_id} price={product.price} qty={product.quantityInStock} discount={product.discount} percentage_reduc={product.percentage_reduc}"
                    )
                )

                continue

        self.stdout.write(f"[{time.ctime()}] Data refresh terminated.")