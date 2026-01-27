import pytest
import requests
from faker import Faker
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture
def random_user():
    fake = Faker()
    return {
        "email": fake.email(),
        "password": "SecurePassword123"
    }

@pytest.fixture(scope="session")
def auth_token():
    fake = Faker()

    auth_user = {
        "email": fake.email(),
        "password": "SecurePassword123"
    }

    # Create user
    create_response = requests.post(
        f"{BASE_URL}/users",
        json=auth_user
    )
    assert create_response.status_code == 200

    # Login
    login_response = requests.post(
        f"{BASE_URL}/login",
        json=auth_user
    )
    assert login_response.status_code == 200

    return login_response.json()["access_token"]
