pip freeze > requirements.txt
chmod +x /path/to/your/entrypoint.sh

docker-compose up -d --build
docker ps -a       # checks status of containers
docker-compose down  # stops and removes containers
docker exec -it django /bin/sh   # opens up an interactive shell 
python manage.py shell



docker stop $(docker ps -aq) # Stop all containers 
docker rm $(docker ps -aq) # Remove all containers 
docker rmi $(docker images -aq) # Remove all images 


# RabbitMQ
http://localhost:15672/#/

# Flower
http://localhost:5555/broker

# Run on Django to inspect task
celery inspect active
celery inspect active queues




# Testing:
done in Python shell

tp1.delay()

# Testing TASK GROUPING:
from celery import group
from worker.tasks import tp1, tp2, tp3, tp4
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()



#                                .s() method
tp1, tp2, tp3, and tp4 are task functions or task methods that you want to execute asynchronously with Celery.
.s() is called on each of these task functions/methods. This .s() method creates a signature for each task, indicating that you want to execute these tasks asynchronously.
The task_group variable now holds a group of task signatures. You can execute this group of tasks together using Celery's group feature. When you call task_group.delay(), it will trigger the execution of tp1, tp2, tp3, and tp4 in parallel as part of the group.

So, .s() is a way to prepare a task for asynchronous execution in Celery by creating a task signature for it. It's a common practice when you want to schedule or group multiple tasks to run concurrently.



# Testing TASK CHAINING:
from celery import chain 
task_chain = chain(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_chain = chain(tp4.s(), tp3.s(), tp2.s(), tp1.s())
task_chain.apply_async()


# Testing TASK Prioritization
from core.celery import t1,t2,t3
t2.apply_async(priority=5, queue='tasks')
t1.apply_async(priority=6, queue='tasks')
t3.apply_async(priority=9, queue='tasks')
t2.apply_async(priority=5, queue='tasks')
t1.apply_async(priority=6, queue='tasks')
t3.apply_async(priority=9, queue='tasks')
t3.apply_async(priority=9, queue='tasks')
t2.apply_async(priority=5, queue='tasks')
t1.apply_async(priority=6, queue='tasks')
t3.apply_async(priority=9, queue='tasks')
priority task 3,1,2