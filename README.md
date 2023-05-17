# Куда пойти? (Where to go?)

Этот сайт - интерактивная карта Москвы, на которую нанесены все известные виды активного отдыха с подробными описаниями и комментариями.  
Пользовательская часть сайта расположена по адресу [where_to_go.pythonanywhere.com](https://where_to_go.pythonanywhere.com).  
Основной вид сайта:  
![user_view](https://github.com/mulchus/where_to_go/assets/111083714/4f6f4268-45b6-4e1c-b0fa-f45489ddc423)

Вход для администраторов и операторов осуществляется по адресу [where_to_go.pythonanywhere.com/admin](https://where_to_go.pythonanywhere.com/admin).  
Вид админки при редактировании места:  
![admin_view](https://github.com/mulchus/where_to_go/assets/111083714/136fffe9-5d92-42dd-ae42-3008d0998e42)


## Установка и запуск

Для запуска сайта у вас уже должен быть установлен Python не ниже 3й версии. 

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и примените все миграции - командой `python manage.py migrate`
- Запустите сервер командой `python manage.py runserver`

Сайт будет работать по ссылке [127.0.0.1:8000](http://127.0.0.1:8000).  


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ = значение`:  
- `SECRET_KEY` — секретный ключ проекта в Django. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.  
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.  
- `ALLOWED_HOSTS` — необходим, если `DEBUG = False`. По умолчанию заданы localhost и 127.0.0.1. [документация Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

**Для запуска проекта следующие настройки менять не требуется, значения проставлены для деплоя.**  
- `SECURE_HSTS_SECONDS = 1` 
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- `SECURE_HSTS_PRELOAD = True`
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_SSL_REDIRECT = True`
[документация по настройкам Django Deployment checklist](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/).


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).  
Данные для сайта взяты с сайта [KudaGo](https://kudago.com/).
