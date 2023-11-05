# Corrected Celery configuration with the correct spelling of "redis" as the backend
import os
from celery import Celery 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

@app.task
def add_numbers():
    return

# Call the autodiscover_tasks method to discover and register tasks from Django apps.
app.autodiscover_tasks()
