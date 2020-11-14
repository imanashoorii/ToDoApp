# ToDoApp

just install dependencies with pip

- pip install -r requirements.txt

and use this application to write your todos

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

----

***You can use this app within Docker with Dockerfile and Compose file included in the project***

- docker build -t python/todoapp .
- docker-compose --compatibility up -d

**Also add your machine or server ip address to ALLOWED_HOSTS in setting.py**
