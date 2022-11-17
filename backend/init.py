# God, please forgive me for what i'm about to code here.
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import psycopg2
import bcrypt
from random import randint

from migrations import runMigrations
import queries
from utils import getRandomString

from ml import prepare, text_classify

from flask_cors import CORS, cross_origin

# import pandas as pd
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.stem import PorterStemmer
# from nltk.stem import WordNetLemmatizer



# SETUP
load_dotenv()

prepare()


salt = bcrypt.gensalt() # but i prefer pepper

connection = psycopg2.connect(
    host=os.environ.get("DATABASE_URL"),
    dbname=os.environ.get("DATABASE_NAME"),
    user=os.environ.get("DATABASE_USERNAME"),
    password=os.environ.get("DATABASE_PASSWORD")
)


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/')
    def home():
        return "TESTXD"

    @app.route('/register', methods=['POST'])
    @cross_origin()
    def register():
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.SELECT_FROM_USERS_BY_EMAIL, (
                    request.json['email'],
                ))
                users = cursor.fetchall()
        if len(users) > 0:
            return 'user with such email already exists', 409

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.ADD_USER, (
                    request.json['name'],
                    request.json['email'],
                    str(bcrypt.hashpw(request.json['password'].encode('utf-8'), salt).decode('utf8')),
                    getRandomString(169)
                ))
        return 'its good byczq', 201

    @app.route('/login', methods=['POST'])
    @cross_origin()
    def login():
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.LOGIN, (
                    request.json['email'],
                ))
                user = cursor.fetchone()
        if user:
            if bcrypt.checkpw(request.json['password'].encode('utf-8'), user[3].encode('utf-8')):
                return {"name": user[1], "email": user[2], "token": user[4]}, 200
            else:
                return 'wrong password byczq', 403
        else:
            return 'wrong email byczq', 404

    # logout is just reseting the user's token. you know. sEcURiTy.
    @app.route('/logout', methods=['POST'])
    @cross_origin()
    def logout():
        if not 'token' in request.json:
            return 'no token byczq', 400

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.LOGOUT, (
                    getRandomString(169),
                    request.json['token']
                ))
        return 'its good byczq', 200


    @app.route('/api/record', methods=['POST'])
    @cross_origin()
    def recordMessage():
        if not 'token' in request.json:
            return 'no token byczq', 400

        if not 'message' in request.json:
            return 'no message byczq', 400

        message = request.json['message']

        happinessValue = text_classify(message)

        happinessValue = happinessValue / 50

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.GET_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                    request.json['token'],
                ))
                recording = cursor.fetchone()

        if recording:
            # recording for today found, we can just update it
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(queries.UPDATE_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                        0 + happinessValue,
                        request.json['token']
                    ))
        else:
            # recording for today not found, we need to create it
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(queries.CREATE_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                        happinessValue,
                        request.json['token']
                    ))

        return {"value": happinessValue}, 201

    @app.route('/api/happiness-today', methods=['GET'])
    @cross_origin()
    def getHappinessToday():
        if not 'token' in request.args:
            return 'no token byczq', 400

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.GET_TODAYS_HAPPINESS_RECORD_FOR_USER, (
                    request.args.get('token'),
                ))
                recording = cursor.fetchone()
        if recording:
            return {"date": recording[2], "value": recording[3]}, 200
        else:
            return {"date": None, "value": None}, 200

    @app.route('/api/happiness', methods=['GET'])
    @cross_origin()
    def getHappiness():
        if not 'token' in request.args:
            return 'no token byczq', 400

        data = []

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.GET_TWO_WEEK_HAPPINESS_RECORDS_FOR_USER, (
                    request.args.get('token'),
                ))
                recordings = cursor.fetchall()

        for record in recordings:
            result = {
                "date": record[2],
                "value": record[3]
            }
            data.append(result)

        return {"data": data}, 200

    return app




# I HATE PYTHON
if __name__ == "__main__":
    runMigrations(connection)

    port = int(os.environ.get('PORT', 5000))

    app = create_app()

    app.run(debug=True, host='0.0.0.0', port=port)
