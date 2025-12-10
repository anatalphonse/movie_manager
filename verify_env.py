import sys
print(f"Python executable: {sys.executable}")
try:
    import dj_database_url
    print("SUCCESS: dj_database_url imported")
except ImportError as e:
    print(f"FAILURE: dj_database_url not found: {e}")

try:
    import whitenoise
    print("SUCCESS: whitenoise imported")
except ImportError as e:
    print(f"FAILURE: whitenoise not found: {e}")
