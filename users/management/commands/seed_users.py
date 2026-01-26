from django.core.management.base import BaseCommand
from users.models import User
from users.constants.seeds import CASHIERS, TECH
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "seed users data"
    
    def handle(self, *args, **options):
        cashier_group, _ = Group.objects.get_or_create(name="Cashier")
        tech_group, _ = Group.objects.get_or_create(name="Tech")


        cashier_created = 0
        tech_created = 0
        
        for data in CASHIERS:
            obj, was_created = User.objects.get_or_create(
                username = data["username"],
                defaults=data
            )
            
            obj.groups.add(cashier_group)
            
            if was_created:
                cashier_created += 1
           
        for data in TECH:
            obj, was_created = User.objects.get_or_create(
                username = data["username"],
                defaults=data
            )
            
            obj.groups.add(tech_group)
            
            if was_created:
                tech_created += 1
           
                
        self.stdout.write(
            self.style.SUCCESS(f"Successfully Seeded {cashier_created} Cahsiers and {tech_created} Tech Users")
        )