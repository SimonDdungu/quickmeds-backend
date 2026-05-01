from django.core.management.base import BaseCommand
from inventory.models import Manufacturer
from inventory.constants.seeds import MANUFACTURERS

class Command(BaseCommand):
    help = "seed manufacturers data"
    
    def handle(self, *args, **options):
        created = 0
        
        for data in MANUFACTURERS:
            obj, was_created = Manufacturer.objects.get_or_create(
                id=data["id"],
                defaults=data
            )
            
            if not was_created:
                continue
            
            if was_created:
                created += 1


        self.stdout.write(
            self.style.SUCCESS(f"Successfully Seeded {created} Manufacturers")
        )