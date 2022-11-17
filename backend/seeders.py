import psycopg2
import os
import bcrypt
from dotenv import load_dotenv
from datetime import datetime, timedelta
from utils import getRandomString
from random import randint, uniform
from datetime import datetime, timedelta


load_dotenv()

salt = bcrypt.gensalt()

connection = psycopg2.connect(
    host=os.environ.get("DATABASE_URL"),
    dbname=os.environ.get("DATABASE_NAME"),
    user=os.environ.get("DATABASE_USERNAME"),
    password=os.environ.get("DATABASE_PASSWORD")
)

CLEAR_USERS = (
    "DELETE FROM happiness_recordings WHERE user_id IN (1,2,3);"
    "DELETE FROM users WHERE id IN (1,2,3);"
)

POPULATE_USERS = (
    "INSERT INTO users (id, name, email, password, token) VALUES (1, 'Grzegorz Brzęczyszczykiewicz', 'grzesiu@gmail.com', '" + str(bcrypt.hashpw('password'.encode('utf-8'), salt).decode('utf8')) + "', '" + getRandomString(169) + "');"
    "INSERT INTO users (id, name, email, password, token) VALUES (2, 'Franz Maurer', 'franz@gmail.com', '" + str(bcrypt.hashpw('password'.encode('utf-8'), salt).decode('utf8')) + "', '" + getRandomString(169) + "');"
    "INSERT INTO users (id, name, email, password, token) VALUES (3, 'Jurek Kiler', 'kiler@gmail.com', '" + str(bcrypt.hashpw('password'.encode('utf-8'), salt).decode('utf8')) + "', '" + getRandomString(169) + "');"
)

POPULATE_HAPPINESS = (
    "INSERT INTO happiness_recordings (user_id, record_date, happiness_level) VALUES (%s, %s, %s);"
)


def happy(cursor):
    for i in range(0, 40):
        d = i % 20
        cursor.execute(POPULATE_HAPPINESS, (
            randint(2, 3),
            datetime.today() - timedelta(days = d),
            uniform(-1, 1)
        ))

with connection:
    with connection.cursor() as cursor:
        cursor.execute(CLEAR_USERS)
        cursor.execute(POPULATE_USERS)
        happy(cursor)
