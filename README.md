# Куда пойти? (Where to go?)

Этот сайт - интерактивная карта Москвы, на которую нанесены все известные виды активного отдыха с подробными описаниями и комментариями.  
Пользовательская часть сайта расположена по адресу [mulch.pythonanywhere.com](https://mulch.pythonanywhere.com).  
Основной вид сайта:  
![user_view](https://github.com/mulchus/where_to_go/assets/111083714/f38d82ec-e166-4bd4-ab84-00b393f1efb2)  

Вход для администраторов и операторов осуществляется по адресу [mulch.pythonanywhere.com/admin](https://mulch.pythonanywhere.com/admin).   

Вид админки при редактировании места:  
![admin_view](https://github.com/mulchus/where_to_go/assets/111083714/9754b656-2f1e-474e-812b-6a12e4842022)  


## Автоматизированная загрузка мест
С помощью команды `load_place` в консоли можно автоматизированно загружать в базу данных новые места.  
Информация о месте должна быть подготовлена в формате JSON со следующими ключами:  
```
{
    "title": "название",
    "imgs": [
            "ссылка на изображение 1", 
            "ссылка на изображение 2", 
            ...
        ],
    "description_short": "короткое описание",
    "description_long": "полное описание в формате HTML",
    "coordinates": {
        "lng": "долгота",
        "lat": "широта"
    }
}
```

Загрузка данных осуществляется следующей командой:  
```
python manage.py load_place "путь/к файлу/о месте.json"
```
например:  
```
python manage.py load_place "https://github.com/.....places/Коворкинг Gravity.json"
```
Если путь к файлу json не содержит пробелов, то его можно не заключать в двойные кавычки.  

В результате скрипт должен вывести в консоли следующую информацию о загрузке (пример):
![загрузка мест](https://github.com/mulchus/where_to_go/assets/111083714/c0fed6eb-10e2-4d98-aea6-86148a1d481c)  


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ = значение`:  
- `SECRET_KEY` — секретный ключ проекта в Django. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.  
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.  
- `ALLOWED_HOSTS` — по умолчанию заданы localhost и 127.0.0.1.  
- `STATIC_ROOT` - папка для сбора статики сайта при размещении на сервере, например "assets". Нельзя задавать "static".  
- `CSRF_TRUSTED_ORIGINS = http://subdomen.domen.com` - домен/субдомен сайта.  
- `SECURE_REDIRECT_EXEMPT = (r'subdomen.domen.com|', )` - домен/субдомен сайта.  
[документация Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

Для запуска проекта следующие настройки менять не требуется, значения проставлены для деплоя. 
- `SECURE_HSTS_SECONDS = 10` 
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- `SECURE_HSTS_PRELOAD = True`
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_SSL_REDIRECT = True`  
[документация по настройкам Django Deployment checklist](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/).


## Установка и запуск

Для запуска сайта у вас уже должен быть установлен Python не ниже 3й версии. 

- Скачайте код
- Создайте файл с переменными окружения.
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и примените все миграции - командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`

Сайт будет работать по ссылке [127.0.0.1:8000](http://127.0.0.1:8000).  


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).  
Данные для сайта взяты с сайта [KudaGo](https://kudago.com/).
