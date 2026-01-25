from django.core.management.base import BaseCommand
from inventory.models import Batch, Medicine, Wholesaler
from inventory.constants.seeds import BATCHES

class Command(BaseCommand):
    help = "seed Wholesalers Data"
    
    def handle(self, *args, **options):
        created = 0
        
        for data in BATCHES:
            try:
                data["medicine"] = Medicine.objects.get(pk=data["medicine"])
                data["wholesaler"] = Wholesaler.objects.get(pk=data["wholesaler"])
            except Medicine.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Medicine with id: {data['medicine']} does not exist. Skipping Batch {data['id']}...")
                )
                continue
            except Wholesaler.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Wholesaler with id: {data['wholesaler']} does not exist. Skipping Batch {data['id']}...")
                )
                continue
                
            
            obj, was_created = Batch.objects.get_or_create(
                medicine = data["medicine"],
                wholesaler = data["wholesaler"],
                batch_number = data["batch_number"],
                defaults=data
            )
            
            if was_created:
                created += 1
            
        self.stdout.write(
            self.style.SUCCESS(f"Successfully Seeded {created} Wholesalers")
        )