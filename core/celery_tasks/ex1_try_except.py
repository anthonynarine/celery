from core.celery_config import app
import logging


@app.task(queue_name="tasks")
def my_task():
    try: