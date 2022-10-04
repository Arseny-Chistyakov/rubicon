# Blog + shop rubicon CRM

---

### Задание

Используя `Django` разработать CRM-систему форум-блога и магазина для корпоративного предприятия ООО "Рубикон"</br>

## Структура

Система представлена приложениями:

- Baskets - приложение для работы с корзиной клиента. [Подробнее Readme.md](baskets/Readme.md)
- Blogs - приложение для работы с блогом. [Подробнее Readme.md](blogs/Readme.md)
- Media - работа с медиафайлами приложений. (Изображение постов, аватарки клиентов)
- Orders - приложение для работы с заказами клиента. [Подробнее Readme.md](orders/Readme.md)
- Products - приложение для работы с продуктами предприятия. [Подробнее Readme.md](products/Readme.md)
- Rubicon - основная структура системы. [Подробнее Readme.md](rubicon/Readme.md)
- Static - работа со статикой системы. (CSS, JS, bootstrap, jquery, fontawesome)
- Users - приложение для работы c клиентами. [Подробнее Readme.md](users/Readme.md)

---

## Установка и настройка

Клонировать проект

```
https://github.com/Arseny-Chistyakov/rubicon.git
```

Создать виртуальное окружение

```
python -m venv venv
```

Активировать виртуальное окружение

```
venv\Scripts\activate.bat
```

Установить зависимости

```
pip install -r requirements.txt
```

Создать .env файл и заполнить

```
SECRET_KEY = 'your value'
#database
TEST_NAME = 'your value'
NAME = 'your value'
USER = 'your value'
PASSWORD = 'your value'
HOST = 'your value'
PORT = 'your value'
#verification_mail
EMAIL_HOST_USER= 'your value'
EMAIL_HOST_PASSWORD= 'your value'
#authorization_social
SOCIAL_AUTH_VK_OAUTH2_KEY= 'your value'
SOCIAL_AUTH_VK_OAUTH2_SECRET= 'your value'
```

Перейти в каталог приложения, создать миграции, применить их

```
python manage.py makemigrations
python manage.py migrate
```

Создать суперпользователя

```
python manage.py createsuperuser
```

Запустить сервер

```
python manage.py runserver
```

---

## License

[MIT License](LICENSE.md) (c) arseny.v.chistyakov