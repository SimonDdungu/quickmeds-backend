from django.core.management.base import BaseCommand
from inventory.models import Wholesaler
from inventory.constants.seeds import WHOLESALER

class Command(BaseCommand):
    help = "seed Wholesalers Data"
    
    def handle(self, *args, **options):
        created = 0
        
        for data in WHOLESALER:
            obj, was_created = Wholesaler.objects.get_or_create(
                id=data["id"],
                defaults = data
            )
            
            if not was_created:
                continue
            
            if was_created:
                created += 1
            
        self.stdout.write(
            self.style.SUCCESS(f"Successfully Seeded {created} Wholesalers")
        )