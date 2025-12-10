import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_manager.settings")
django.setup()

from movies.models import MovieInfo
print("\n--- DATA CHECK ---")
for m in MovieInfo.objects.all():
    print(f"Title: {m.title}")
    print(f"Year: {m.year} (Type: {type(m.year)})")
    print(f"Censor: {m.censor_details}")
    if m.censor_details:
        print(f"  Rating: {m.censor_details.rating}")
print("--- END CHECK ---")
