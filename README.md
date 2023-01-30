# Foodgram
![yamdb_workflow](https://github.com/Maksim-Afonin/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Описание

Foodgram - продуктовый помощник для публикации рецептов и не только)) 

Помимо создания рецептов, можно подписываться на рецепты других пользователей, а также на понравившихся авторов. 

Можно добавлять рецепты в избранное, а также в список покупок, чтобы затем скачать список в PDF файле. 

## Стек технологий

- Python
- Django
- Django REST framework
- Docker
- PostreSQL
- Nginx
- gunicorn

## Запуск в Docker контейнерах

Установите Docker.

Склонировать проект с git
```
https://github.com/Maksim-Afonin/foodgram-project-react.git
```

В директории infra/ необходимо создать файл .env:
```
cd infra
touch .env
```

В котором требуется указать переменные окружения, пример:
```
echo SECRET_KEY=************ >> .env

echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo DB_HOST=db  >> .env

echo DB_PORT=5432  >> .env
```

В директории infra/, в файле nginx.conf измените адрес(ip/домен), необходимо указать адрес вашего сервера.

Запустите docker compose
```
docker-compose up -d --build
```

Примените миграции
```
docker-compose exec backend python manage.py migrate
```

Загрузите ингредиенты
```
docker-compose exec backend python manage.py load_ingrs
```

Создайте суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```

Далее соберите статику
```
docker-compose exec backend python manage.py collectstatic --noinput
```

## Сайт

Ознакомится как выглядит и работает сат можно по ссылке - http://foodgram-bryansk.ddns.net/

## Документация API

Документация по API доступна по ссылке  http://foodgram-bryansk.ddns.net/api/docs/


# Есть вопросы? Контакты:

Telegram - https://t.me/Afonin_Maksim

Email - webmaster.bryansk@yandex.ru