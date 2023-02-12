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
- Filtering movies and movie sessions.


## Testing

- Run tests using different approach: `docker-compose run app sh -c "python manage.py test"`;
- If needed, also check the flake8: `docker-compose run app sh -c "flake8"`.


## Download image from Docker Hub

The command to pull the image: `docker pull viktorbeniukh/cinema_api-app:latest`.
