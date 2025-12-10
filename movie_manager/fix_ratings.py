import os
import django
import sys
import random

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_manager.settings")
django.setup()

from movies.models import MovieInfo

print("Converting ratings to numeric...")
for m in MovieInfo.objects.all():
    if m.censor_details:
        current_rating = m.censor_details.rating
        # Check if it looks like "PG-13" or non-numeric
        if not current_rating or not current_rating.replace('.', '', 1).isdigit():
            # Assign a random score between 5.0 and 9.9 for demo
            new_score = f"{random.uniform(5.5, 9.5):.1f}"
            print(f"Update {m.title}: '{current_rating}' -> '{new_score}'")
            m.censor_details.rating = new_score
            m.censor_details.save()
        else:
            print(f"Skipping {m.title}: already numeric '{current_rating}'")

print("Data update complete.")
