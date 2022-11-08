from flask import Flask, render_template, session, request
import os
from dotenv import load_dotenv
import psycopg2

from migrations import runMigrations
from queries import SELECT_FROM_USERS_BY_ID, ADD_USER
from utils import getRandomString



# SETUP
load_dotenv()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # secret! dont look at it!

connection = psycopg2.connect(
    host=os.environ.get("DATABASE_URL"),
    dbname=os.environ.get("DATABASE_NAME"),
    user=os.environ.get("DATABASE_USERNAME"),
    password=os.environ.get("DATABASE_PASSWORD")
)




# ROUTING
@app.route('/')
def home():
    return "TESTXD"

@app.route('/users/<int:id>')
def show_user(id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_FROM_USERS_BY_ID, (id,))
            record = cursor.fetchone()
            print(record)
    return {"id": record[0], "name": record[1], "email": record[2], "token": record[3]}, 200

@app.route('/register', methods=['POST'])
def store_user():
    token = getRandomString(128)
    print(token)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_USER, (
                request.json['name'],
                request.json['email'],
                request.json['password'], # TODO Hash it xd
                token
            ))
    return 'ok', 201




# I HATE PYTHON
if __name__ == "__main__":
    runMigrations(connection)

    port = int(os.environ.get('PORT', 5000))

    app.run(debug=True, host='0.0.0.0', port=port)