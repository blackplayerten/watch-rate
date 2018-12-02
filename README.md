# watch-rate

Запуск:

1. Установить зависимости из `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Запустить PostgreSQL на 5432 порту (в случае доккер-контейнера):

    ```bash
    docker start postgresql
    ```
    
    Если нет контейнера, то запустить из образа:
    
    ```bash
    docker run -p 5432:5432 --name postgres postgres:alpine
    ```
    
    В нем должна быть создана БД `films`
    
3. Применить миграции:

    ```bash
    python manage.py migrate
    ```
    
4. Запустить nginx с конфигом `watch_rate.conf`.

5. Запустить gunicorn:

    ```bash
    gunicorn -b 127.0.0.1:8080 watch_rate.wsgi:application
    ```
