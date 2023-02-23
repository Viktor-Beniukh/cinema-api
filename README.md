# Cinema API

API service for cinema management written on DRF

### Installing using GitHub

Install PostgreSQL and create db

```shell
git clone https://github.com/Viktor-Beniukh/cinema-api.git
cd cinema_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set POSTGRES_HOST=<your db hostname>
set POSTGRES_NAME=<your db name>
set POSTGRES_USER=<your db username>
set POSTGRES_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver   
```
You need to create `.env` file and add there the variables with your according values: 
- `POSTGRES_HOST`: this is host name for databases;
- `POSTGRES_NAME`: this is databases name;
- `POSTGRES_USER`: this is username for databases;
- `POSTGRES_PASSWORD`: this is username password for databases;
- `SECRET_KEY`: this is Django Secret Key - by default is set automatically when you create a Django project.
                You can generate a new key, if you want, by following the link: `https://djecrety.ir`.


## Run with docker

Docker should be installed

- Create docker image: `docker-compose build`
- Run docker app: `docker-compose up`


## Getting access

- Create user via /api/user/register/
- Get access token via /api/user/token/


## Features

- JWT authentication;
- Admin panel /admin/;
- Documentation is located at /api/doc/swagger/;
- Managing orders and tickets;
- Creating movies with genres, actors;
- Creating cinema halls;
- Adding movie sessions;
- Filtering actors, genres, cinema halls, movies and movie sessions.

### How to create superuser
- Run `docker-compose up` command, and check with `docker ps`, that 2 services are up and running;
- Create new admin user. Enter container `docker exec -it <container_name> bash`, and create in from there;

### What do APIs do
- [GET] /api/cinema/actors/ - obtains a list of actors with the possibility of filtering by last name;
- [GET] /api/cinema/genres/ - obtains a list of actors with the possibility of filtering by name;
- [GET] /api/cinema/movie_sessions/ - obtains a list of movie sessions with the possibility of filtering 
        by date and movie id;
- [GET] /api/cinema/movies/ - obtains a list of movies with the possibility of filtering by actors & genres lists 
        and movie title;
- [GET] /api/cinema/cinema_halls/ - obtains a list of cinema halls with the possibility of filtering by name;
- [GET] /api/cinema/orders/ - browses users order history page;
- [POST] /api/cinema/actors/ - creates an actor;
- [POST] /api/cinema/genres/ - creates a genre;
- [POST] /api/cinema/movies/ - creates a movie;
- [POST] /api/cinema/cinema_halls/ - creates a cinema hall;
- [POST] /api/cinema/orders/ - creates orders;

### Checking the endpoints functionality
- You can see detailed APIs at swagger page: `http://127.0.0.1:8000/api/doc/swagger/`.


## Testing

- Run tests using different approach: `docker-compose run app sh -c "python manage.py test"`;
- If needed, also check the flake8: `docker-compose run app sh -c "flake8"`.


## Download image from Docker Hub

The command to pull the image: `docker pull viktorbeniukh/cinema_api-app:latest`.


## Check project functionality

User credentials for test the functionality of this project:
- email address: `migrated@user.com`;
- password: `userpassword`.
