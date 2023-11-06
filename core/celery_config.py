# Corrected Celery configuration with the correct spelling of "redis" as the backend
import os
import time
from celery import Celery 
from kombu import Queue, Exchange



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY") 

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "core", "celery_tasks" )

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and filename.endswith(".py"):
            module_name = f"core.celery_tasks.{filename[:-3]}"
            
            module = __import__(module_name, fromlist=["*"])
            
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")


    app.autodiscover_tasks(task_modules)  


# @app.task(queue_name="tasks")
# def t1():
#     time.sleep(3)
    
# @app.task(queue_name="tasks")
# def t2():
#     time.sleep(3)
    
# @app.task(queue_name="tasks")
# def t3():
#     time.sleep(3)


# app.conf.task_routes = {"worker.tasks.task1": {"queue":"queue1"}, "worker.tasks.task2": {"queue":"queue2"}}
# Configure Celery's broker transport options
# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),  # Define priority levels from 0 to 9
#     "step": ":",                        # Define the separator for priority in task names
#     "queue_order_strategy": "priority",  # Define the queue order strategy as "priority"
# }


# Call the autodiscover_tasks method to discover and register tasks from Django apps.

