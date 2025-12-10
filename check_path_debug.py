import os
import sys

# Add current dir to path just in case
sys.path.append(os.getcwd())

import settings
print(f"BASE_DIR: {settings.BASE_DIR}")
static_path = settings.BASE_DIR / 'static'
print(f"Static path: {static_path}")
print(f"Static exists: {os.path.exists(static_path)}")
