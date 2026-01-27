import requests
import faker
import logging

fake = faker.Faker()

logger = logging.getLogger(__name__)
BASE_URL = "http://127.0.0.1:8000"

def test_login_unregistered_email():
    logger.info("Sending request to login with unregistered email")

    response = requests.post(
        f"{BASE_URL}/login",
        json={"email": fake.email(), "password": fake.password()}
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

    assert response.status_code == 401

def test_create_user_duplicate_email_and_invalid_passoword_login():
    email = fake.email()
    password = fake.password(length=12)
    payload = {"email": email, "password": password}
    
    # create user first time
    first = requests.post(f"{BASE_URL}/users", json=payload)

    # first creation should go through
    assert first.status_code == 200
    
    logger.info("Sending request to create a user account with existing email")
    # create duplicate user
    duplicate = requests.post(f"{BASE_URL}/users", json=payload)

    logger.info(f"Response status: {duplicate.status_code}")
    logger.info(f"Response body: {duplicate.json()}")

    # duplicate user creation should raise exception
    assert duplicate.status_code == 400

    logger.info("Sending request to login with invalid password")

    response = requests.post(
        f"{BASE_URL}/login",
        json={"email": email, "password": fake.password()}
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

    assert response.status_code == 401

def test_get_nonexistent_user():
    logger.info("Sending request to retrive nonexistent user info")
    response = requests.get(f"{BASE_URL}/users/999999")

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")
    
    assert response.status_code == 404
