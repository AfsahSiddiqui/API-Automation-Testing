import requests
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User
from app.auth import verify_password
import logging

fake = Faker()
engine = create_engine("sqlite:///./test.db")
Session = sessionmaker(bind=engine)

logger = logging.getLogger(__name__)
BASE_URL = "http://127.0.0.1:8000"

def test_create_user_and_validate_db():
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True)

    logger.info("Sending request to create user")
    response = requests.post(
        f"{BASE_URL}/users",
        json={"email": email, "password": password}
    )

    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

    assert response.status_code == 200
    assert response.json()["email"] == email

    db = Session()

    logger.info("Querying the database to verify user creation")
    user = db.query(User).filter(User.email == email).first()

    assert user is not None
    assert user.email == email
    assert verify_password(password,user.hashed_password)

    logger.info("Verification completed")

    db.close()
