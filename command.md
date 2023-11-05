pip freeze > requirements.txt
chmod +x /path/to/your/entrypoint.sh

docker-compose up -d --build
docker ps -a       << checks status of containers
docker-compose down  << stops and removes containers
docker exec -it django /bin/sh   << opens up an interactive shell 
python manage.py shell

