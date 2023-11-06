import imp
from core.celery_config import app


@app.task(queue_name="tasks")
def my_task1():
    ...
    
@app.task(queue_name="tasks")
def my_task2():
    ...