from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "seed all database records"
    
    def handle(self, *args, **options):
        
        self.stdout.write("seeding the database....")
        
        call_command("seed_users")
        call_command("seed_manufacturers")
        call_command("seed_medicine")
        call_command("seed_wholesaler")
        call_command("seed_batch")
        
        
        self.stdout.write(
            self.style.SUCCESS(f"Seeding complete")
        )