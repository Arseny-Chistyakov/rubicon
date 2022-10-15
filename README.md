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

Особенности и решения:

- На данном релизе корзина создается для каждого товара и пользователя отдельно, в следующей версии разрабатывается
  связь M2M для моделей `product` и `basket` для реализации одной общей корзины пользователя
- На данном релизе функционал приложения `orders` не доведен до совершенства. Где-то недоработаны шаблоны, некоторый
  функционал может работать не стабильно, в следующей версии разрабатывается более красивое и функциональное приложение
  `orders`
- На данном релизе поддерживается авторизация через соц. сеть `VK`, в следующей версии разрабатывается поддержка и
  других популярных соц. сетей
- На данном релизе при регистрации новый пользователь должен пройти верификацию аккаунта с помощью своего `email`

---

## Установка и настройка

Клонировать проект

```
https://github.com/Arseny-Chistyakov/rubicon.git
```

Создать виртуальное окружение

Linux/MacOS:

```
source venv/bin/activate
```

Windows:

```
venv/Scripts/activate.bat     
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
<br>

Для проверки работы CRM можно установить заготовленные фикстуры c помощью команд:
###### Фикстура - это набор данных, которые Django умеет импортировать в базу данных.
Пользователи:
```
python manage.py loaddata users/fixtures/Users.json 
```
Категории продуктов:
```
python manage.py loaddata products/fixtures/ProductCategory.json 
```
Продукты:
```
python manage.py loaddata products/fixtures/Products.json 
```
Записи постов:
```
python manage.py loaddata blogs/fixtures/Posts.json
```
Можно объединить команды в одну:
```
python manage.py loaddata users/fixtures/Users.json && python manage.py loaddata products/fixtures/ProductCategory.json && python manage.py loaddata products/fixtures/Products.json && python manage.py loaddata blogs/fixtures/Posts.json
```

---

## License

[MIT License](LICENSE.md) (c) arseny.v.chistyakov