import requests
from tests.conftest import BASE_URL, logger

def test_login_unregistered_email(random_user):
    logger.info("Sending request to login with unregistered email")

    response = requests.post(
        f"{BASE_URL}/login",
        json=random_user
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

    assert response.status_code == 401

def test_create_user_duplicate_email_and_invalid_passoword_login(random_user):
    payload = random_user
    email = payload["email"]
    
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
        json={"email": email, "password": "WrongPassword123!"}
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

    assert response.status_code == 401

