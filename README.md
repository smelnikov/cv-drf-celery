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

    curl -i -H 'Accept: application/json' http://localhost:8000/api/pages/?page=2

    >>>

    HTTP 200 OK
    Allow: GET
    Content-Type: application/json
    Vary: Accept

    {
        "count": 345,
        "next": "http://127.0.0.1:8000/api/pages/?page=3",
        "previous": "http://127.0.0.1:8000/api/pages/",
        "results": [
            {
                "url": "http://127.0.0.1:8000/api/pages/101/",
                "title": "Whether prevent lawyer ask left east factor."
            },
        ]
    }

## Получить страницу

```http
GET /api/pages/<id>/
```

### Пример

    curl -i -H 'Accept: application/json' http://localhost:8000/api/pages/101/

    >>>

    HTTP 200 OK
    Allow: GET
    Content-Type: application/json
    Vary: Accept

    {
        "url": "http://127.0.0.1:8000/api/pages/101/",
        "content": [
            {
                "title": "Spring trial thus act drop guy.",
                "pos": 0,
                "counter": 0,
                "path": "http://richardson.com/home/later.mov",
                "subtitle": "https://price-torres.org/terms.htmanyone.srt"
            },
            {
                "title": "Ball body bill PM.",
                "pos": 1,
                "counter": 0,
                "path": "http://rice-cooper.com/main/about.htmlborn.mov",
                "subtitle": "https://miller-bush.com/usually.srt"
            },
            {
                "title": "Painting staff create play this civil summer.",
                "pos": 2,
                "counter": 0,
                "path": "https://leon-wilson.com/post.htmthrow.webm",
                "subtitle": "https://www.webb-cox.net/search/go.srt"
            }
        ],
        "title": "Response consider green understand stay."
    }
