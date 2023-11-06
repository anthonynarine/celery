from datetime import timedelta
from core.celery_config import app
from celery.schedules import crontab


app.conf.beat_schedule = {
    #     'task1':{
#         'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task1',
#         'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'),
#         'kwargs': {'foo': 'bar'},
#         'args': (1, 2),
#         'options': {
#             'queue':'tasks',
#             'priory':5,
#         }
#     },
#     'task2':{
#         'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task2',
#         'schedule': timedelta(seconds=10),
#     }

    "task1": {
        "task": "core.celery_tasks.ex3_task_schedule_customization.task1",
        "schedule": crontab(),   # this runs every minute by default
        "kwargs": {"foo":"fighter"},
        "args": (1,2),
        "options": {
            "queue":"tasks",
            "priority": 5,
        }
    },
    "task2": {
        "task": "core.celery_tasks.ex3_task_schedule_customization.task2",
        "schedule": timedelta(seconds=25),
    },
}

@app.task(queue="tasks")
def task1(a ,b, **kwargs):
    result = a + b
    print(f"Running task 1 - {result}")
    
    
@app.task(queue="tasks")
def task2():
    print("Running task 2")
    
    
    
    
