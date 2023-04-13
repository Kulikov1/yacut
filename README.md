# Ускоритель ссылок YaCut
Проект предназначен для укорачивания ссылок переданных пользователем.\
Пользователь может придумать короткое имя для ссылки сам(не более 16 символов),\
либо довериться случаю и проект сделает све за вас. Случайное имя будет состоять из\
6 букв латиницы в верхнем и нижнем регистре и цифр в случайном порядке.\
Короткие имена уникальные и не могут повторяться.

## Примеры работы

* ### Оригинальная ссылка 1
    ```
    https://test.com
    ```
    ### Вывод программы:
    ```
    https://yacut.com/output
    ```
* ### Оригинальная ссылка 2:
    ```
    https://test.com
    короткое имя: example
    ```
    ### Вывод программы:
    ```
    http://yacut.com/example
    ```
## Установка проекта
Клонировать репозиторий и перейти в него в командной строке:


```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Примеры запросов API:

### Запрос:

*Получение короткой ссылки*

**POST** http://localhost/api/id/
```
{
  "url": "https://test.com/djfngjdfngbiourebhdbfghbdosfbgusd",
  "custom_id": "string"
}
```
### Ответ:
```
{
  "url": "https://test.com",
  "short_link": "http://yacut.com/string"
}
```
### Запрос:

*Получение оригинальной ссылки по короткому имени*

**GET** http://yacut.com/string
### Ответ:
```
{
  "url": "https://test.com/djfngjdfngbiourebhdbfghbdosfbgusd"
}
```