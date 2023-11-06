from core.celery_config import app
import logging

"""
from core.celery_tasks.ex1_try_except import my_task
my_task.delay()
"""


# logging.basicConfig(filename="app.log", level=logging.ERROR, 
# format="%(acetime)s %(levelname)s %(message)s")

@app.task(queue_name="tasks")
def my_task():
    try:
        raise ConnectionError("Connection Error Occurred...")
    except ConnectionError:
        logging.eror("Connection error occured....")
        raise ConnectionError