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
JSON:
{
	"phone": "+79009006565",
	"cod_phone": "900",
	"tag": "test_tag"
}

Добавить рассылку:

POST:
```sh
$ http://localhost:8000/add_mailing
```
JSON:
{
    "date_time_mailing": "2024-01-24 12:52:11",
    "message_text": "test_text_message",
    "filter": "test_lilter",
    "end_date_time_mailing": "2024-01-24 12:52:11"
}
