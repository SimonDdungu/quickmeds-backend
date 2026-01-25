from django.core.management.base import BaseCommand
from inventory.models import Medicine, Manufacturer
from inventory.constants.seeds import MEDICINE

class Command(BaseCommand):
    help = "seed medicine data"
    
    def handle(self, *args, **options):
        created = 0
        
        
        for data in MEDICINE:
            
            try:
                data["manufacturer"] = Manufacturer.objects.get(pk=data["manufacturer"])
            except Manufacturer.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Manufacturer with id: {data['manufacturer']} does not exist. Skipping Medicine {data['name']}...")
                )
                continue
            
            obj, was_created = Medicine.objects.get_or_create(
                name=data["name"],
                generic_name=data["generic_name"],
                strength=data["strength"],
                strength_unit=data["strength_unit"],
                defaults=data 
            )
            
            if was_created:
                created += 1


        self.stdout.write(
            self.style.SUCCESS(f"Successfully Seeded {created} Medicine")
        )