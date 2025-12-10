from django.core.management.base import BaseCommand
from movies.models import MovieInfo, CensorInfo

class Command(BaseCommand):
    help = 'Fixes missing movie data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Checking movies...")
        for m in MovieInfo.objects.all():
            changed = False
            if not m.year:
                m.year = 2023
                changed = True
                self.stdout.write(f"Updated year for {m.title}")
            
            if not m.censor_details:
                c = CensorInfo.objects.create(rating="PG-13", certified="U/A")
                m.censor_details = c
                changed = True
                self.stdout.write(f"Created CensorInfo for {m.title}")
            
            if changed:
                m.save()
            
            self.stdout.write(f"Movie: {m.title} | Year: {m.year} | Censor: {m.censor_details}")
