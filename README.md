<h1 align="center"> Проект реализующий API для системы опроса пользователей. </h1>

<h2 align="center"> 1. Техническое задание. </h2>

<p>
Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.

Результат выполнения задачи:
- исходный код приложения в github (только на github, публичный репозиторий)
- инструкция по разворачиванию приложения (в docker или локально)
- документация по API

</p>

<h2 align="center"> 2. Инструкция по разворачиванию проекта. </h2>

* Клонировать проект с GitHub

````
https://github.com/LeonMaxwell/polling-master.git
````

* Настраиваем виртуальное окружение

````
/usr/bin/python3 -m venv venv
source venv/bin/activate
````

* Устанавливаем библиотеки, которые требуются для запуска проекта
```
pip install -r requeriments.txt
```

* Делаем миграцию базы данных
```
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

* Создаем суперпользователя
```
python manage.py createsuperuser
```
* Запускаем проект
```
python manage.py runserver
```

<h2 align="center"> 3. Документация API. </h2>

<p> 
Для документирования API была использована библиотека drf-yasg2.
Просмотр документации доступен по ссылке: <a>http://127.0.0.1:8000/swagger/</a>
</p>


<b>Создание опроса</b>

* Request method: POST
* URL: http://127.0.0.1:8000/poll/create/
* Body:
  * name: 
    * type: string
    * title: Имя опроса
    * maxLength: 255
    * minLength: 1
  * description:
    * type: string
    * title: Описание опроса
    * minLength: 1
  * created_at:
    * type: string(date-time)
    * title: Дата начала опроса
  * finish_at:
    * type: string(date-time)
    * title: Дата окончания опроса

```
curl -X POST "http://127.0.0.1:8000/poll/create/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls" -d "{  \"name\": \"string\",  \"description\": \"string\",  \"created_at\": \"string(date-time)\",  \"finish_at\": \"string(date-time)\"}"
```


<b>Получение списка активных опросов</b>

* Request method: GET
* URL: http://127.0.0.1:8000/poll/

```
curl -X GET "http://127.0.0.1:8000/poll/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls"
```

<b>Получение определенного опроса</b>

* Request method: GET
* URL: http://127.0.0.1:8000/poll/pk/
* Body:
  * pk: 
    * type: string
    * title: ID опроса

```
curl -X GET "http://127.0.0.1:8000/poll/pk/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls"
```

<b>Обновление определенного опроса</b>

* Request method: PUT
* URL: http://127.0.0.1:8000/poll/pk/
* Body:
  * pk: 
    * type: string
    * title: ID опроса
  * Body:
  * name: 
    * type: string
    * title: Имя опроса
    * maxLength: 255
    * minLength: 1
  * description:
    * type: string
    * title: Описание опроса
    * minLength: 1
  * created_at:
    * type: string(date-time)
    * title: Дата начала опроса
  * finish_at:
    * type: string(date-time)
    * title: Дата окончания опроса
```
curl -X GET "http://127.0.0.1:8000/poll/pk/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls" -d "{  \"name\": \"string\",  \"description\": \"string\",  \"created_at\": \"string(date-time)\",  \"finish_at\": \"string(date-time)\"}"
```


<b>Удаление опроса</b>

* Request method: DELETE
* URL: http://127.0.0.1:8000/poll/pk/
* Body:
  * pk: 
    * type: string
    * title: ID опроса
    * 
```
curl -X DELETE "http://127.0.0.1:8000/poll/2/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls"
```

<b>Создание вопроса</b>

* Request method: POST
* URL: http://127.0.0.1:8000/question/create/
* Body:
  * poll: 
    * type: integer
    * title: Опрос
  * text:
    * type: string
    * title: Текст вопроса
    * minLength: 1
  * type:
    * type: integer
    * title: Type {Enum: [1,2,3]}

```
curl -X POST "http://127.0.0.1:8000/question/create/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls" -d "{  \"poll\": poll,  \"text\": \"text\",  \"type\": type}"
```

<b>Получение вопроса</b>

* Request method: GET
* URL: http://127.0.0.1:8000/question/pk/
* Body:
  * pk: 
    * type: integer
    * title: ID вопроса
    
```
curl -X GET "http://127.0.0.1:8000/question/pk/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls"
```

<b>Изменение вопроса</b>

* Request method: PUT
* URL: http://127.0.0.1:8000/question/pk/
* Body:
  * pk:
    * type: integer
    * title: ID вопроса
  * poll: 
    * type: integer
    * title: Опрос
  * text:
    * type: string
    * title: Текст вопроса
    * minLength: 1
  * type:
    * type: integer
    * title: Type {Enum: [1,2,3]}

```
curl -X POST "http://127.0.0.1:8000/question/pk/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls" -d "{  \"poll\": poll,  \"text\": \"text\",  \"type\": type}"
```

<b>Удаление вопроса</b>

* Request method: DELETE
* URL: http://127.0.0.1:8000/question/pk/
* Body:
  * pk: 
    * type: integer
    * title: ID вопроса
    
```
curl -X DELETE "http://127.0.0.1:8000/question/pk/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls"
```

<b>Прохождение опроса</b>

* Request method: POST
* URL: http://127.0.0.1:8000/vote/
* Body:
  * question: 
    * type: integer
    * title: Вопрос
  * text:
    * type: string
    * title: Текст ответа
    * minLength: 1
  * anon:
    * type: boolean
    * title: Anon

```
curl -X POST "http://127.0.0.1:8000/vote/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls" -d "{  \"question\": question,  \"text\": \"text\",  \"anon\": anon}"
```

<b>Получение опросов пользователей</b>

* Request method: GET
* URL: http://127.0.0.1:8000/poll/passed/pk/
* Body:
  * pk: 
    * type: integer
    * title: ID пользователя
    
```
curl -X GET "http://127.0.0.1:8000/poll/passed/pk/" -H  "accept: application/json" -H  "X-CSRFToken: 8Y8rFDx9f91fKnoqy7wAkTX83TZTV49tbXWIme2t0g7FKO4Cvb0spQfwrzZEoRls"
```