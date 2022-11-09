import pytest
import json

from init import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


def test_request_example(test_client):
    response = test_client.get("/")
    assert b"TESTXD" in response.data

def test_registering_works(test_client):
    response = test_client.post("/register", json={
        "name": "pariusz mostol",
        "email": "lot@of.experience",
        "password": "web69iscool",
    })
    assert response.status_code == 201

def test_registering_email_unique_works(test_client):
    response = test_client.post("/register", json={
        "name": "pariusz mostol",
        "email": "lot@of.experience",
        "password": "web69iscool",
    })
    assert response.status_code == 409

def test_login_works(test_client):
    response = test_client.post("/login", json={
        "email": "lot@of.experience",
        "password": "web69iscool",
    })

    global token
    token = json.loads(response.data)['token']

    assert response.status_code == 200

def test_login_password_check_works(test_client):
    response = test_client.post("/login", json={
        "email": "lot@of.experience",
        "password": "web2137iscool",
    })
    assert response.status_code == 403

def test_login_email_check_works(test_client):
    response = test_client.post("/login", json={
        "email": "notalot@of.experience",
        "password": "web69iscool",
    })
    assert response.status_code == 404

def test_logout_token_check_works(test_client):
    response = test_client.post("/logout", json={
        "some_random": "data"
    })
    assert response.status_code == 400

def test_record_token_check_works(test_client):
    response = test_client.post("/api/record", json={
        "message": "some random message"
    })
    assert response.status_code == 400

def test_record_token_check_works(test_client):
    response = test_client.post("/api/record", json={
        "token": "some random token"
    })
    assert response.status_code == 400

def test_record_positive_works(test_client):
    response = test_client.post("/api/record", json={
        "token": token,
        "message": "positive message"
    })
    assert response.status_code == 201

def test_record_neutral_works(test_client):
    response = test_client.post("/api/record", json={
        "token": token,
        "message": "neutral message"
    })
    assert response.status_code == 201

def test_record_negative_works(test_client):
    response = test_client.post("/api/record", json={
        "token": token,
        "message": "negative message"
    })
    assert response.status_code == 201

def test_record_positive_the_sequel_works(test_client):
    response = test_client.post("/api/record", json={
        "token": token,
        "message": "positive message"
    })
    assert response.status_code == 201

def test_happiness_today_works(test_client):
    response = test_client.get("/api/happiness-today", json={
        "token": token
    })
    assert response.status_code == 200
    assert response.json["value"] == "0.02"

def test_happiness_today_token_check_works(test_client):
    response = test_client.get("/api/happiness-today", json={
        "message": "some random message"
    })
    assert response.status_code == 400