from datetime import timedelta
from core.celery_config import app


app.conf.beat_schedule = {
    "task1": {
        "task": "core.celery_tasks.ex2_task_scheduling.task1",
        "schedule": timedelta(seconds=5),
    },
    "task2":{
        "task": "core.celery_tasks.ex2_task_scheduling.task2",
        "schedule": timedelta(seconds=25),
    },
}

@app.task(queue_name="tasks")
def task1():
    print("Running task 1")
    
    
@app.task(queue_name="tasks")
def task2():
    print("Running task 2")