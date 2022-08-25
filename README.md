# Development

## 1. create .env.development in root directory, and write it
```
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
MYSQL_HOST=db
MYSQL_DATABASE=db

PYTHONPATH=/usr/src/app/app

GITHUB_ACCESS_TOKEN=

STATIC_URL = http://localhost:10001
AUTH_SECRET_KEY = ###
```
In AUTH_SECRET_KEY, you should add secret_key value obtained by the following command
```
openssl rand -hex 32
```

## 2. exec below
```
docker network create fastapi_network
```

## 3. exec below
```docker-compose build --no-cache```

## 4. exec below
```docker-compose up```

## 5. Access to below URL, then you can see API.
```
http://localhost:10445/docs
```


# Migrations
## 1. exec below and run commands in the container
```
$ docker-compose run api bash

api$ cd /usr/src/app/db
api$ alembic upgrade head
```

# Seeding
exec below in the api container
```
$api cd ../db
$api python seed.py
```
