# Simple Django REST Framework with Celery integration

# Quickstart

Установить Docker
 
https://docs.docker.com/compose/install/

Cборка:

    docker-compose build

Запуск тестов:

    docker-compose up autotests

Запуск Django+celery:

    docker-compose up runserver

Наполнение демо-данными:

    docker-compose up demo_pages

# REST API

## Получить список всех страниц

```http
GET /api/pages/
```


### Пример

    curl -i -H 'Accept: application/json' http://localhost:8000/api/pages

    >>>

    HTTP/1.1 200 OK
    Date: Fri, 21 Feb 2020 12:06:10 GMT
    Server: WSGIServer/0.2 CPython/3.8.0
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET
    X-Frame-Options: SAMEORIGIN
    Content-Length: 2

    [
        {
            "url": "http://127.0.0.1:8000/api/pages/1/",
            "title": "Пробная страница"
        }
    ]

## Получить страницу

```http
GET /api/pages/<id>/
```

### Пример

    curl -i -H 'Accept: application/json' http://localhost:8000/api/pages/1/

    >>>

    HTTP/1.1 200 OK
    Date: Fri, 21 Feb 2020 12:12:31 GMT
    Server: WSGIServer/0.2 CPython/3.8.0
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET
    X-Frame-Options: SAMEORIGIN
    Content-Length: 540

    {
        "url": "http://127.0.0.1:8000/api/pages/1/",
        "content": [
            {
                "title": "Video",
                "pos": 0,
                "counter": 21,
                "path": "http://foo.bar/path/to/video",
                "subtitle": "http://foo.bar/path/to/subtitle"
            },
            {
                "title": "Short description",
                "pos": 1,
                "counter": 21,
                "value": "Unbelievable short description.."
            },
            {
                "title": "Full description",
                "pos": 2,
                "counter": 21,
                "value": "Wow! This is really full. Please don't wast your time for reading this."
            },
            {
                "title": "Audio",
                "pos": 3,
                "counter": 21,
                "path": "http://foo.bar/path/to/audio",
                "bitrate": 128000
            }
        ],
        "title": "Пробная страница"
    }
