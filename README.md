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

## Уровни доступа пользователей:
Гость (неавторизованный пользователь)
Авторизованный пользователь
Администратор

## Что могут делать неавторизованные пользователи
- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.

## Что могут делать авторизованные пользователи
- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

## Что может делать администратор- 
Администратор обладает всеми правами авторизованного пользователя. 
Плюс к этому он может:
- изменять пароль любого пользователя,
- создавать/блокировать/удалять аккаунты пользователей,
- редактировать/удалять любые рецепты,
- добавлять/удалять/редактировать ингредиенты.
- добавлять/удалять/редактировать теги.

## Документация API
Примеры запросов:
Для регистрации пользователя, необходимо отправить POST запрос на адрес:
```
http://foodgram-bryansk.ddns.net/api/users/
```
Тело запроса
```
{
    "email": "vpupkin@yandex.ru",
    "username": "vasya.pupkin",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "password": "Qwerty123"
}
```

Для получения токена, следует отправить POST запрос на адрес:
```
http://foodgram-bryansk.ddns.net/api/auth/token/login/
```
Тело запроса
```
{
    "password": "string",
    "email": "string"
}
```

Получить список рецептов можно отправив GET запрос на эндпоинт:
```
http://foodgram-bryansk.ddns.net/api/recipes/
```

Чтобы создать новый рецепт нужно отправить POST запрос на адрес(Доступно только с токеном):
```
http://foodgram-bryansk.ddns.net/api/recipes/
```

Тело запроса
```
{
    "ingredients": [
        {
        "id": 1123,
        "amount": 10
        }
    ],
    "tags": [
        1,
        2
    ],
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
    "name": "string",
    "text": "string",
    "cooking_time": 1
}
```

Полная документация по API доступна по ссылке  http://foodgram-bryansk.ddns.net/api/docs/


# Есть вопросы? Контакты:

Telegram - https://t.me/Afonin_Maksim

Email - webmaster.bryansk@yandex.ru