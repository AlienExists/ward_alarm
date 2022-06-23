Ready to run On Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/AlienExists/ward_alarm)

---

**Stages for the first launch**

1. source venv/Scripts/activate
2. *pip install -r requirements.txt*
3. python3 db_create.py
4. python3 db_migrate.py

---

***Subsequent launches***

1. python3 wsgi.py