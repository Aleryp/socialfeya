<h2 align="center">SocialFeya by AleRyp</h2>

Соц. мережа на Django

- [Telegram](https://t.me/AleRyp)
- [Tweeter](https://twitter.com/AleRypDJN)
### Використано
- Python  (^3.8)
- Django Rest Framework
- Postgres

## Початок роботи з проектом

##### 1 - Створити образ і запустити контейнер

    docker-compose up --build
    
######Якщо потрібно, то запуск від імені супер користувача(sudo)

##### 2 - Перейти сюди:

    http://127.0.0.1:8000/api/v1/swagger/

## Docker,розробка
###### При потребі всі команди зупускати від імені супер користувача(sudo)
##### 1 - Зробити форк репозиторія

##### 2 - Клонувати репозиторій

    git clone лінк_на_згенерований_репозиторій

##### 3 - В корені проекту створити файл .env.dev

    DEBUG=1
    SECRET_KEY=fdsadqw3f32wg<43g3hv$%#@%F$F$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    POSTGRES_DB=socialfeya
    
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=socialfeya
    POSTGRES_USER=socialfeya_user
    POSTGRES_PASSWORD=socialfeya_pass
    POSTGRES_HOST=socialfeya-db
    POSTGRES_PORT=5432
    
    DATABASE=postgres

##### 4 - Створити образ і запустити контейнер

    docker-compose up --build
    
##### 5 - Створити супер-юзера

    docker exec -it socialfeya_socialfeya_back_1 bash
    python manage.py createsuperuser
                                                        
##### 6 - Якщо потрібно, очистити БД.

    docker-compose down -v
 

Copyright (c) 2020-****, AleRyp - Kozynets Andrian






