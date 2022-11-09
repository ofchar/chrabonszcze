# God, please forgive me for what i'm about to code here.
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import psycopg2
import bcrypt
from random import randint

from migrations import runMigrations
from queries import SELECT_FROM_USERS_BY_ID, ADD_USER, LOGIN, GET_TODAYS_HAPPINESS_RECORD_FOR_USER, CREATE_TODAYS_HAPPINESS_RECORD_FOR_USER, UPDATE_TODAYS_HAPPINESS_RECORD_FOR_USER
from utils import getRandomString



# SETUP
load_dotenv()

app = Flask(__name__)

salt = bcrypt.gensalt() # but i prefer pepper

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

@app.route('/register', methods=['POST'])
def register():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_USER, (
                request.json['name'],
                request.json['email'],
                str(bcrypt.hashpw(request.json['password'].encode('utf-8'), salt).decode('utf8')),
                getRandomString(169)
            ))
    return 'jest git byczq', 201

@app.route('/login', methods=['POST'])
def login():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(LOGIN, (
                request.json['email'],
            ))
            user = cursor.fetchone()
    if user:
        if bcrypt.checkpw(request.json['password'].encode('utf-8'), user[3].encode('utf-8')):
            return {"name": user[1], "email": user[2], "token": user[4]}, 200
        else:
            return 'zle haslo byczq', 403
    else:
        return 'zly email byczq', 404

@app.route('/logout', methods=['POST'])
def logout():
    return 'nah', 500

@app.route('/api/record', methods=['POST'])
def recordMessage():
    message = request.json['message']

    # Dear @mlExperts, in line below we need to assign a value -1, 0 or 1 to the happinessValue based on message variable
    # (which obviously is message from the user). -1 for negative, 0 for neutral and 1 for positive.
    # After that is working please remove the randint line.
    # happinessValue = MLMODEL(message)
    happinessValue = randint(-1, 1)

    happinessValue = happinessValue / 50
    print(happinessValue)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                request.json['token'],
            ))
            recording = cursor.fetchone()

    if recording:
        # recording for today found, we can just update it
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                    0 + happinessValue,
                    request.json['token']
                ))
    else:
        # recording for today not found, we need to create it
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                    happinessValue,
                    request.json['token']
                ))

    return 'jest git byczq', 201




# I HATE PYTHON
if __name__ == "__main__":
    runMigrations(connection)

    port = int(os.environ.get('PORT', 5000))

    app.run(debug=True, host='0.0.0.0', port=port)