**Этапы для певого запуска**

1. source venv/Scripts/activate
2. *pip install -r requirements.txt*
3. python3 db_create.py
4. python3 db_migrate.py

***Последующие запуски***

1. python3 wsgi.py