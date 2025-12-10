import os
import django
import sys

# Add the project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_manager.settings")
django.setup()

from movies.models import MovieInfo, CensorInfo

print("Fixing data...")
movies = MovieInfo.objects.all()
for m in movies:
    print(f"Checking {m.title}...")
    if not m.year:
        print(f"  Setting year for {m.title} to 2023")
        m.year = 2023
    
    if not m.censor_details:
        print(f"  Creating CensorInfo for {m.title}")
        c = CensorInfo.objects.create(rating="PG-13", certified="U/A")
        m.censor_details = c
    
    m.save()
    print(f"  Updated: {m.title} - Year: {m.year}, Rating: {m.censor_details.rating}")

print("Done.")
