import os
import sys
import django

# Add the parent directory (where manage.py is) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Tell Django where the settings module is
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lecture_manager.settings')

# Setup Django
django.setup()

from lectures.models import Lecture

print(Lecture.objects.all())