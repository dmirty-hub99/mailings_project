# Mailings project
API для создания пользователей и рассылок

## Использование

Создать миграции:
```sh
$ docker-compose run webapp python manage.py migrate
```

Создать пользователя:
```sh
$ docker-compose run webapp python manage.py createsuperuser
```

Запустить все контейнеры:
```sh
$ docker-compose up
```
## Маршруты

Все клиенты:

GET:
```sh
$ http://localhost:8000/all_clients
```

Все рассылки:

GET:
```sh
$ http://localhost:8000/all_mailings
```

Все письма:

GET:
```sh
$ http://localhost:8000/all_messages
```

Добавить пользователя:

POST:
```sh
$ http://localhost:8000/add_client
```

Добавить рассылку:

POST:
```sh
$ http://localhost:8000/add_mailing
```
